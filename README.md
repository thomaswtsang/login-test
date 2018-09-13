# e2e-login-demo

Demo of end-to-end browser testing with pytest and selenium.

## Setup
### Install browser driver
On Mac OS:
```
brew install geckodriver
```

### Install test dependencies
```
python3.6 -m venv env
source env/bin/activate

make deps
```

## Run tests
```
make test
```

## Notes
### How it works
- test steps are all in `test_login.py`
- setup and teardown of the browser driver are managed by pytest fixtures
- `page_objects.py` abstracts the login page to locators and page actions
- user profiles for a good and bad user are stored in `consts.py`

### Assumptions
- unit tests for frontend and backend cover input permutation (e.g., input sanitation)
- unit tests should also cover input lengths
- user is not locked out after multiple failed attempts
- not checking for error dialog because unable to reset password
