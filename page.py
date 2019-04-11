import webbrowser
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from fields import status_fields,value_fields

#lh-audit
# Values  
#lh-audit--binary
#lh-audit--numeric

# Binary Classess
# lh-audit--fail 
# lh-audit--pass
# lh-audit--average

# Numeric
# lh-audit__display-text
def parsePage(urlToOpen):
    result = dict()
    chrome_options = Options()  
    chrome_options.add_argument("--headless") 
    browser = webdriver.Chrome(chrome_options=chrome_options)
    page = browser.get(urlToOpen)

    try:
        # content = browser.find_element_by_class_name('lh-guage_percentage')
        content = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,'lh-gauge__percentage'))
        )
       # print(content.get_attribute('innerHTML'))
    finally:
        print('Done')

    diagonistc = browser.find_elements_by_class_name('lh-audit')
    foundFields = []
    for diagon in diagonistc:
        itemClass = diagon.get_attribute('class')
        titleEl = diagon.find_element_by_class_name('lh-audit__title')
        title = titleEl.get_attribute('textContent')
        if title in "|".join(foundFields):
            continue
        fieldValue = ''
        foundFields.append(title)
        # if title in "|".join(status_fields):            
        if "lh-audit--fail" in itemClass:
            fieldValue = 'Critical'
        elif "lh-audit--average" in itemClass:
            fieldValue = 'Average'
        elif "lh-audit--pass" in itemClass:
            fieldValue = 'Good'
            # print(title, ' - ', fieldValue )
            
        # if title in "|".join(value_fields):
        if "lh-audit--informative" in itemClass:
            fieldValue = diagon.find_element_by_class_name('lh-audit__display-text').get_attribute('textContent')

        result[title] = fieldValue
    browser.close()
    return result
