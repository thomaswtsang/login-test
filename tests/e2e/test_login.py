
class TestLoginPage(object):
    
    def test_login_success(self, LoginPageObject):
        LoginPageObject.login()
        assert LoginPageObject.is_logged_in()

    def test_login_failure(self):
        pass
