from tests.e2e.consts import test_user, bad_user

class TestLoginPage(object):
    
    def test_login_success(self, LoginPageObject):
        LoginPageObject.login(**test_user)
        assert LoginPageObject.is_logged_in()

    def test_login_failure(self, LoginPageObject):
        LoginPageObject.login(**bad_user)
        assert not LoginPageObject.is_logged_in()

    def test_remember_me(self, LoginPageObject):
        LoginPageObject.login(remember=True, **test_user)
        LoginPageObject.load()
        assert LoginPageObject.is_logged_in()

