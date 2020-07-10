<?php 
$vars = "again,dgain,shutter,iso,awbred,awbblue".split(",");
$output = "";
foreach($vars as $var){
	$output.="{$var}=".strval(floatval($_GET[$var])).";";
}
file_put_contents("./ramdisk/settings",$output);