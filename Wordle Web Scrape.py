#Imports
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = '/usr/local/bin/chromedriver' 
service = Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://eslforums.com/5-letter-words/')
li_elements = driver.find_elements(By.TAG_NAME, 'li')
five_letter_words = [
    li.text.split()[0].strip() 
    for li in li_elements 
    if li.text and len(li.text.split()[0].strip()) == 5]
df = pd.DataFrame(five_letter_words, columns=['Words'])

# Print the DataFrame
df.to_excel("Five_Letter_Words.xlsx")
#print(df)
