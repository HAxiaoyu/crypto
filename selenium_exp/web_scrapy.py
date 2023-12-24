from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = 'D:\download\chrome-109\chromedriver-win64\chromedriver.exe'

def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)

# Open the website
browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")

# Extract all projects
projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

# Extract information for each project
project_list = {}
for p in projects:
    project_name = p.text
    project_url = p.find_elements(By.XPATH, "a")[0].get_attribute('href')
    project_list[project_name] = project_url

# Close connection
browser.quit()

# Extracting data
project_df = pd.DataFrame.from_dict(project_list, orient = 'index')

# Manipulate the table
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)

# Export project dataframe to CSV
project_df.to_csv('project_list.csv')