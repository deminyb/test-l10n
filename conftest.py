import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Choose language')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_argument(f"lang={language}")
    print(f"\nStarting browser with language = {language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()