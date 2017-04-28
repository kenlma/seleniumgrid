from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

#driver = webdriver.PhantomJS(service_log_path='/var/log/phantomjs/ghostdriver.log')  # Optional argument, if not specified will search path.
driver = webdriver.Remote(
    command_executor="http://192.168.0.125:4444/wd/hub",
    desired_capabilities={
        "browserName": "firefox"
    }
)
driver.get('http://www.google.com/xhtml');
#time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
print (driver.current_url)
time.sleep(5) # Let the user actually see something!
driver.quit()