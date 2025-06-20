from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # Initialize the Chrome driver
    service = Service()
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
