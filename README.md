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
