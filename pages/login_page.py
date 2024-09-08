from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Name")
        self.password_input = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.login_button = page.get_by_role("button", name="Signup")
        self.cookie_accept_button = page.get_by_label("Consent", exact=True)  # Локатор кнопки принятия куки

    def navigate(self):
        self.page.goto("https://automationexercise.com/login")

    def accept_cookies(self):
        if self.cookie_accept_button.is_visible():  # Проверяем видимость кнопки
            self.cookie_accept_button.click()  # Кликаем по кнопке, если она видна

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()
