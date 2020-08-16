<?php
$i = shell_exec("ip -f inet -br addr | grep -i 'UP' | sed 's/\s\+/,/g' | cut -d, -f3 | cut -d/ -f1 | head -n1");
echo($i);


?>
