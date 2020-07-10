
<?php
$tilt = intval($_GET['tilt']);
$pan = intval($_GET['pan']);
if($pan>=0){
        exec("echo 0={$pan}%>/dev/servoblaster");
        echo("echo 0={$pan}%>/dev/servoblaster");
}
if($tilt>=0){
        exec("echo 1={$tilt}%>/dev/servoblaster");
        echo("echo 1={$tilt}%>/dev/servoblaster");
}
