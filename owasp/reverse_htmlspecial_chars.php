<?php
echo( "chars to decode: ");
$ch = fgets(STDIN);
echo(htmlspecialchars_decode($ch, ENT_QUOTES));


?>

