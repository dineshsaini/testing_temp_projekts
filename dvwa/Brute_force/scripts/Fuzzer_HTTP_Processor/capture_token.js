// Auxiliary variables/constants needed for processing.
var count = 1;

/**
 * Processes the fuzzed message (payloads already injected).
 * 
 * Called before forwarding the message to the server.
 * 
 * @param {HttpFuzzerTaskProcessorUtils} utils - A utility object that contains functions that ease common tasks.
 * @param {HttpMessage} message - The fuzzed message, that will be forward to the server.
 */
function processMessage(utils, message) {
	// To obtain the list of payloads:
	//    utils.getPayloads()
	// To obtain original message:
	//    utils.getOriginalMessage()
	// To stop fuzzer:
	//    utils.stopFuzzer()
	// To increases the error count with a reason:
	//    utils.increaseErrorCount("Reason Error Message...")
	// To send a message, following redirects:
	//    utils.sendMessage(myMessage)
	// To send a message, not following redirects:
	//    utils.sendMessage(myMessage, false)
	// To add a message previously sent to results:
	//    utils.addMessageToResults("Type Of Message", myMessage)
	// To add a message previously sent to results, with custom state:
	//    utils.addMessageToResults("Type Of Message", myMessage, "Key Custom State", "Value Custom State")
	// The states' value is shown in the column 'State' of fuzzer results tab
	// To get the values of the parameters configured in the Add Message Processor Dialog.
	//    utils.getParameters() 
	// A map is returned, having as keys the parameters names (as returned by the getRequiredParamsNames()
	// and getOptionalParamsNames() functions below)
	// To get the value of a specific configured script parameter
	//    utils.getParameters().get("exampleParam1")

	// Process fuzzed message...
	var TreeSet = Java.type("java.util.TreeSet")
	var HtmlParameter = Java.type("org.parosproxy.paros.network.HtmlParameter")
	var URLEncoder = Java.type("java.net.URLEncoder");
	
	user_token = org.zaproxy.zap.extension.script.ScriptVars.getGlobalVar("gvar.user_token");
	if (user_token == null)
		user_token = "";
	
	
	print("Process fuzzed message::user_token :: " + user_token);
	print("message.getURLParams()::"+message.getUrlParams());
	
	p = new TreeSet();
	
	var it = message.getUrlParams().iterator();

	while(it.hasNext()){
		param = it.next()
		var val = param.getValue();
		if (param.getName().equals("user_token")){
			val = URLEncoder.encode(user_token, "UTF-8");
		}
		
		p.add(new HtmlParameter(HtmlParameter.Type.url, param.getName(), val));
	}
	
	message.setGetParams(p);
	print("message.getRequestHeader():: " + message.getRequestHeader());
}

/**
 * Processes the fuzz result.
 * 
 * Called after receiving the fuzzed message from the server.
 * 
 * @param {HttpFuzzerTaskProcessorUtils} utils - A utility object that contains functions that ease common tasks.
 * @param {HttpFuzzResult} fuzzResult - The result of sending the fuzzed message.
 * @return {boolean} Whether the result should be accepted, or discarded and not shown.
 */
function processResult(utils, fuzzResult){
	// All the above 'utils' functions are available plus:
	// To raise an alert:
	//    utils.raiseAlert(risk, confidence, name, description)
	// To obtain the fuzzed message, received from the server:
	//    fuzzResult.getHttpMessage()
	// To get the values of the parameters configured in the Add Message Processor Dialog.
	//    utils.getParameters() 
	// A map is returned, having as keys the parameters names (as returned by the getRequiredParamsNames()
	// and getOptionalParamsNames() functions below)
	// To get the value of a specific configured script parameter
	//    utils.getParameters().get("exampleParam1")
	var Matcher = Java.type("java.util.regex.Matcher");
	var Pattern = Java.type("java.util.regex.Pattern");
	
	var srchptrn = '<input type=\'hidden\' name=\'user_token\' value=\'([^\']+)\' />';
	var sstring = fuzzResult.getHttpMessage().getResponseBody().toString();

	print ("getResponseHeader():: " + fuzzResult.getHttpMessage().getResponseHeader());

	r = Pattern.compile(srchptrn);
	m = r.matcher(sstring);
	var user_token = "";

	if(m.find()){
		user_token = m.group(1);
		print('found:: ' + user_token);
	}else{
		print("not found");
	}

	org.zaproxy.zap.extension.script.ScriptVars.setGlobalVar("gvar.user_token", user_token);
	return true;
} 


/**
 * This function is called during the script loading to obtain a list of the names of the required configuration parameters,
 * that will be shown in the Add Message Processor Dialog for configuration. They can be used
 * to input dynamic data into the script, from the user interface
*/
function getRequiredParamsNames(){
	return [];
}

/**
 * This function is called during the script loading to obtain a list of the names of the optional configuration parameters,
 * that will be shown in the Add Message Processor Dialog for configuration. They can be used
 * to input dynamic data into the script, from the user interface
*/
function getOptionalParamsNames(){
	return [];
}


