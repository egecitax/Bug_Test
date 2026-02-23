import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://app.s4e.io/sign-in"


def test_tc02_password_visibility_toggle(page: Page):
    """
    TC02: Şifre gizle/göster (göz) ikonunun düzgün çalışıp çalışmadığını test eder.
    """
    page.goto(BASE_URL)

    password_input = page.locator("#auth-element-sign-in-password")
    password_input.fill("GizliSifre123!")

    expect(password_input).to_have_attribute("type", "password")

    toggle_icon = page.locator('svg:has(path[d^="M15.29"])')
    toggle_icon.click()

    expect(password_input).to_have_attribute("type", "text")


@pytest.mark.skip(
    reason="BLOCKED: Cloudflare Captcha koruması 'Login' butonunu disabled bıraktığı için otomasyon ile tıklanamıyor.")
def test_tc06_empty_fields_validation(page: Page):
    """
    TC06: E-posta ve şifre alanları boşken 'Login' butonuna tıklandığında
    uyarı verilip verilmediğini kontrol eder.
    """
    page.goto(BASE_URL)
    page.get_by_role("button", name="Login").click()

    email_error = page.locator("#auth-element-sign-in-email-helper-text")
    password_error = page.locator("#auth-element-sign-in-password-helper-text")

    expect(email_error).to_be_visible()
    expect(email_error).to_have_text("Email is required")

    expect(password_error).to_be_visible()
    expect(password_error).to_have_text("Password is required")


@pytest.mark.skip(
    reason="BLOCKED: Cloudflare anti-bot sistemi test otomasyonunu engelliyor, manuel test veya bypass token gerekiyor.")
def test_tc04_invalid_credentials(page: Page):
    """
    TC04: Yanlış şifre ile giriş denemesi.
    """
    page.goto(BASE_URL)

    page.locator("#auth-element-sign-in-email").fill("teststajyer@s4e.io")
    page.locator("#auth-element-sign-in-password").fill("YanlisSifre123!")

    page.get_by_role("button", name="Login").click()


def test_tc07_email_field_type_bug(page: Page):
    """
    BUG-001: Email alanının type niteliği 'email' olmalıdır.
    Not: Bu test, sistemdeki mevcut bir UI hatasını (type="text" olması)
    kanıtlamak için yazılmıştır. Geliştirici bu bug'ı çözene kadar test FAILED olacaktır.
    """
    page.goto(BASE_URL)

    email_input = page.locator("#auth-element-sign-in-email")

    # Beklentimiz type niteliğinin "email" olmasıdır.
    # Sistemde "text" olduğu için Playwright burada hatayı (bug'ı) yakalayacak.
    expect(email_input).to_have_attribute("type", "email")