from page_objects import PageObject, PageElement


class LoginPage(PageObject):
    # username needs a more unique identifier
    username = PageElement(class_name="text-input")
    password = PageElement(id_="password2")
    submit = PageElement(class_name="green-button")
    remember_me = PageElement(id_="remember_me")

    url_slug = "/login"

    def load(self):
        self.get(self.url_slug)

    def fill_in_form(self, **profile):
        self.username = profile.get("username")
        self.password = profile.get("password")

    # ideally page actions are moved to a client class
    def login(self, remember=False, **profile):
        self.fill_in_form(**profile)

        if remember:
            self.remember_login()

        self.submit.click()

    def is_logged_in(self):
        return "events" in self.w.current_url

    def remember_login(self):
        self.remember_me.click()

    def clear_cookies(self):
        self.w.delete_all_cookies()
