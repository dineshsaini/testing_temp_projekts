<?php

function toUTF7($text){
    return mb_convert_encoding($text, 'UTF-7');
}

function toUTF8($text){
    return mb_convert_encoding($text, 'UTF-8');
}

echo("Enter text to convert: ");
$txt = fgets(STDIN);

echo("****<<UTF-7>>****\n");
echo(toUTF7($txt));
echo(htmlspecialchars(toUTF7($txt)));
echo("****<<UTF-8>>****\n");
echo(toUTF8($txt));
echo(htmlspecialchars(toUTF8($txt)));



?>
