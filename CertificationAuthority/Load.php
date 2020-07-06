<?php

$Value = $_POST["value"];

$Pieces = explode(",", $Value);

$Filename = $Pieces[1] . ".txt";

$Content = file_get_contents($Filename);
$CompareTo = $Pieces[0];

if ($Content === $CompareTo) {
	echo "VERIFICATO";
}

?>