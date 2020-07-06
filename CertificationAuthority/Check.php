<?php

$Value = $_POST["value"];

$Pieces = explode(",", $Value);

$Filename = $Pieces[1] . ".txt";

if (is_writable($Filename)) {

    if (!$File = fopen($Filename, 'w')) {
         echo "Cannot open file $Filename";
         exit;
    }

    if (fwrite($File, $Pieces[0]) === FALSE) {
        echo "Cannot write to file $Filename";
        exit;
    }

    echo "CARICATO";

    fclose($File);

} else {
    echo "The file $Filename is not writable";
}

?>


