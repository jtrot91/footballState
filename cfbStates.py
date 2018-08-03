from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def makeSoup(url):
	driver = webdriver.Firefox()
	driver.get(url)
	html = driver.page_source
	driver.close()
	return BeautifulSoup(html, "html.parser")

if __name__ == "__main__":
	teamPage = makeSoup("http://www.winsipedia.com/team")
	teams = teamPage.findAll('a', href=True)
	print(teams)