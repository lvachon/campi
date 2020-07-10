<?php 
$vars = explode(",","shutter,iso,awbred,awbblue,exposure");
$output = "";
foreach($vars as $var){
	if($var!="exposure"){
		$output.="{$var}:".strval(floatval($_GET[$var])).";";
	}else{
		$output.="{$var}:".$_GET[$var].";";
	}
}
file_put_contents("./ramdisk/settings",$output);