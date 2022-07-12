# from time import sleep
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# import requests
# from bs4 import BeautifulSoup
#
#
# def flight_center_scrapper():
#     url = "https://secure.flightcentre.com.au/SroMfzKd/results"
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, 'html5lib')
#     print(r.content)
#     table = soup.find('div', {'class': 'test-combinedResultsApp'})\
#         .find('div', {'class': 'test-PaginatorGroups'})
#     print(table)
#     #
#     # for row in table.findAll('div', attrs={'class': 'test-tripGroup trip-group'}):
#     #     airline = row.find_next('div', attrs={'class': 'test-journeyLogos singleLogo-0-295'})['title']
#     #     print(airline)
