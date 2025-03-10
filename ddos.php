<?php
// Figlet komutunu tanımla
$command = "figlet FLK";

// Komutu çalıştır ve çıktısını al
$output = [];
$return_var = 0;
exec($command, $output, $return_var);

// Çıktıyı ekrana yazdır
if ($return_var === 0) {
    echo implode("\n", $output);
} else {
    echo "Figlet komutu çalıştırılırken bir hata oluştu.\n";
}
?>