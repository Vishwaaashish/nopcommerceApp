from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        driver.maximize_window()
        print("Launching chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        print("Launching firefox browser")

    else:
        driver=webdriver.Edge()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata = {
        'distribution_name': 'nop Commerce',
        'author': 'John Doe',
        'Tester':'Aashish'
        # Add more metadata as needed
    }

# it is hook for delete/modify Environment Info to html Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Java_Home",None)
#     metadata.pop("Plugins", None)


# # conftest.py
# import pytest
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config._metadata = {
#         'distribution_name': 'MyDistribution',
#         'author': 'John Doe',
#         # Add more metadata as needed
#     }
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_html_report_title(report):
#     report.title = "My Test Report"
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.append(f"Custom Metadata: {prefix[0].config._metadata}")
#     prefix.append(f"Distribution Name: {prefix[0].config._metadata['distribution_name']}")
#
# # Optionally, you can customize the HTML report further by adding more hook implementations.





















