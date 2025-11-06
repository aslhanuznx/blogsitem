<?php
if($_SERVER["REQUEST_METHOD"] == "POST") {
    $isim = htmlspecialchars($_POST['isim']);
    $email = htmlspecialchars($_POST['email']);
    $mesaj = htmlspecialchars($_POST['mesaj']);

    
    $to = "auzefuz@gmail.com";
    $subject = "Yeni iletişim mesajı - $isim";
    
    $body = "İsim: $isim\n";
    $body .= "Email: $email\n\n";
    $body .= "Mesaj:\n$mesaj\n";

    $headers = "From: $email";

    if(mail($to, $subject, $body, $headers)){
        echo "<p>Mesajınız gönderildi! Teşekkürler.</p>";
    } else {
        echo "<p>Maalesef mesaj gönderilemedi. Lütfen tekrar deneyin.</p>";
    }
}
?>
