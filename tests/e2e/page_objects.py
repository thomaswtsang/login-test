from page_objects import PageObject, PageElement

class LoginPage(PageObject):
    # username needs a more unique identifier
    username = PageElement(class_name = "text-input")
    password = PageElement(id_ = "password2")
    submit = PageElement(class_name = "green-button")
    
    def fill_in_form(self):
        # TODO abstract user input
        self.username = "qacandidate@splashthat.com"
        self.password = "testingislife"

    def login(self):
        self.fill_in_form()
        self.submit.click()

    def is_logged_in(self):
        return "events" in self.w.current_url
