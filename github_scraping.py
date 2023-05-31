import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set the path to the HTML file
html_file_path = 'FILE_PATH_TO_HTML_FILE'

# Set up Selenium webdriver
driver_service = Service('/bin/chromedriver_mac64')
driver = webdriver.Chrome(service=driver_service)
# Ref: https://www.selenium.dev/documentation/webdriver/drivers/service/

# Load the HTML file using the file:// protocol
driver.get('file://' + html_file_path)
# Ref: https://www.selenium.dev/documentation/


time.sleep(5)

# Find the elements using their respective CSS selectors
elements_1 = driver.find_elements(By.CSS_SELECTOR, 'a.color-fg-muted.d-inline-block.ml-1')
elements_2 = driver.find_elements(By.CSS_SELECTOR, 'span.annotation-title.flex-auto.pr-2')
elements_3 = driver.find_elements(By.CSS_SELECTOR, 'div.py-2.pl-4.ml-3.overflow-auto')
# Ref: https://bharateeshd.gitbook.io/seleniumatoz/selenium/locators/css-selectors

# Create a list to store the extracted data
data = []

# Extract the data from the elements
for i in range(len(elements_1)):
    file = elements_1[i].text
    name = elements_2[i].text
    description = elements_3[i].text
    data.append([file, name, description])

# Generate a timestamp for the CSV file name
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#Ref: https://www.programiz.com/python-programming/datetime/current-datetime

# Define the CSV file path with the timestamp
csv_file_path = f'FILE_PATH_TO_CSV_FILE/file_{timestamp}.csv'

# Write the data to a CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['file', 'name', 'description'])  # Write the header row
    writer.writerows(data)  # Write the data rows
# Ref: https://www.pythontutorial.net/python-basics/python-write-csv-file/

# Close the browser
driver.quit()


