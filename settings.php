<?php 
$vars = explode(",","shutter,iso,awbred,awbblue");
$output = "";
foreach($vars as $var){
	$output.="{$var}=".strval(floatval($_GET[$var])).";";
}
file_put_contents("./ramdisk/settings",$output);