Bug Raporu (Bug Report)
Sayfada yapılan analizler sonucunda aşağıdaki hata tespit edilmiş ve otomasyon koduna başarısız (FAILED) olacak bir test olarak (test_tc07_email_field_type_bug) eklenmiştir.

Bug ID: BUG-001

Title: Login sayfasındaki E-posta giriş alanında type="email" yerine type="text" kullanılmış (Mobil UX ve HTML5 Validasyon eksikliği)

Severity: Minor

Environment: Tüm Tarayıcılar, https://app.s4e.io/sign-in

Steps to Reproduce:

https://app.s4e.io/sign-in adresine gidin.

"Email Address" alanına sağ tıklayıp "İncele" (Inspect) seçeneği ile DOM yapısını açın.

<input id="auth-element-sign-in-email" ...> elementinin type özelliğini kontrol edin.

Expected Result:
Mobil cihazlarda e-posta klavyesinin açılması ve tarayıcı tabanlı temel format doğrulamalarının çalışabilmesi için alanın <input type="email"> olması beklenir.

Actual Result:
Alan <input type="text"> olarak tanımlanmıştır.