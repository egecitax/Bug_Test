# Anchor Security Yazılım Danışmanlık A.Ş. - Test Engineering Internship Task

Bu depo, Anchor Security Yazılım Danışmanlık A.Ş. Test Mühendisliği stajyer değerlendirme süreci kapsamında hazırlanmıştır. Projede `https://app.s4e.io/sign-in` modülü incelenmiş, test senaryoları çıkarılmış, Playwright (Python) ile otomasyon süreçleri yazılmış ve UI tabanlı bir bug raporlanmıştır.

##  1. Test Senaryoları (Test Cases & Edge Cases)

Giriş sayfası için aşağıdaki senaryolar tasarlanmış ve manuel/otomatize olarak incelenmiştir:

**Pozitif Senaryolar (Happy Path):**
* **TC01:** Kayıtlı e-posta, doğru şifre ve başarılı Captcha doğrulaması ile sisteme giriş yapılabilmesi.
* **TC02:** Şifre alanındaki "göz" (gizle/göster) ikonuna tıklandığında şifrenin maskesiz görünmesi ve tekrar tıklandığında maskelenmesi.
* **TC03:** Sosyal Login (Google, Microsoft, GitHub) butonlarının ilgili yetkilendirme sayfalarına yönlendirmesi.

**Negatif Senaryolar & Edge Cases:**
* **TC04:** Geçerli e-posta fakat yanlış şifre girildiğinde sistemin uyarı vermesi.
* **TC05:** Kayıtlı olmayan bir e-posta adresi ile giriş denemesi.
* **TC06:** Alanlar boş bırakılarak "Login" butonuna tıklandığında `Email is required` ve `Password is required` validasyon mesajlarının alınması.
* **TC08 (Edge Case):** E-posta adresinin başına veya sonuna boşluk (space) eklendiğinde sistemin bu boşlukları `trim()` ile temizleyerek giriş yapabilmesi.

---

##  2. Otomasyon (Playwright & Pytest)

Otomasyon testleri **Python**, **Playwright** ve **Pytest** kullanılarak `test_login.py` dosyası içerisinde yazılmıştır.

### Kurulum ve Çalıştırma

1. Repoyu klonlayın:
   ```bash
   git clone <sizin_repo_linkiniz>
   cd <repo_klasor_adi>
   
2. Sanal ortam (virtual environment) oluşturun ve aktif edin:

Bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

3. Gerekli kütüphaneleri ve tarayıcıları yükleyin:

Bash
pip install -r requirements.txt
playwright install

4. Testleri çalıştırın:

Bash
pytest test_login.py -v --headed
 
Otomasyon Notları (Cloudflare & Anti-Bot Koruması)

Testler çalıştırılırken, Login butonu etkileşimleri (TC04 ve TC06) Cloudflare Turnstile (Captcha) bot koruması sebebiyle disabled durumda kalmaktadır. Bu durum otomasyon framework'lerinde beklenen bir davranış olduğundan, bu testler pytest.mark.skip ile bloklanmış (BLOCKED) statüsüne alınarak raporda belirtilmiştir. Gerçek bir CI/CD ortamında bu testlerin koşulabilmesi için test ortamlarında Captcha'nın deaktif edilmesi veya bypass token sağlanması gerekmektedir.