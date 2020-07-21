<?php
echo( "chars to encode: \n");
$ch = fgets(STDIN);
echo(htmlspecialchars($ch, ENT_QUOTES, 'UTF-8'));


?>

