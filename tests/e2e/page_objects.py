from page_objects import PageObject, PageElement

class LoginPage(PageObject):
    username = PageElement(name = "data[User][email]")
    password = PageElement(id_ = "password2")
    submit = PageElement(class_name = "green-button")
    
    def fill_in_form(self):
        pass

    def login(self):
        pass
