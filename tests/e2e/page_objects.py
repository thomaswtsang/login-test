from page_objects import PageObject, PageElement

class LoginPage(PageObject):
    # username needs a more unique identifier
    username = PageElement(class_name = "text-input")
    password = PageElement(id_ = "password2")
    submit = PageElement(class_name = "green-button")
    remember_me = PageElement(id_ = "remember_me")
    
    def fill_in_form(self, **profile):
        self.username = profile.get("username")
        self.password = profile.get("password")

    # ideally page actions are moved to a client class
    def login(self, **profile):
        self.fill_in_form(**profile)
        self.submit.click()

    def is_logged_in(self):
        return "events" in self.w.current_url
