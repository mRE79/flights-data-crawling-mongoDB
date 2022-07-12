# from time import sleep
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
# from selenium.webdriver.chrome import options
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from datetime import date
# import datetime
# import flight
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# def emirates_scrapper(driver):
#
#     url = "https://www.emirates.com/ir/english/"
#
#     # Emirates
#     driver.get(url)
#
#     driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div["
#                                   "1]/div/div[1]/div/div/div[1]/div/input").send_keys("Tehran (IKA)")
#
#     driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div[4]/div[1]/div["
#                                   "1]/div/div[2]/div/div/div[1]/div/input").send_keys("Melbourne (MEL)")
#
#     # continue button
#     sleep(5)
#     search_button = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div[2]"
#                                                   "/div/div/section/div[4]/div[2]/div[3]/form/button")
#     driver.execute_script("arguments[0].click();", search_button)
#     sleep(2)
#     # try:
#     #     wait.until(ec.element_to_be_clickable(driver.find_element(
#     #         By.CLASS_NAME, "cta cta--large cta--primary "
#     #         "js-continue-search-flight "
#     #         "search-flight__continue--cta "))).click()
#     # except (NoSuchElementException, TimeoutException):
#     #     pass
#
#     sleep(2)
#     button = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/div["
#                                            "4]/div[1]/div[3]/eol-datefield/div[1]/div[1]/input")
#     driver.execute_script("arguments[0].click();", button)
#     sleep(2)
#
#     print("select date search options")
#     flexable_date_button = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/"
#                                                          "section/div[4]/div[1]/div[3]/eol-datefield/eol-calendar/"
#                                                          "div/div/div[1]/div/label[1]/input")
#     driver.execute_script("arguments[0].click();", flexable_date_button)
#     sleep(2)
#     # wait.until(ec.element_to_be_clickable(driver.find_element(
#     #     By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section"
#     #               "/div[4]/div[1]/div[3]/eol-datefield/eol-calendar/div/div/div[1]/"
#     #               "div/label[1]/input"))).click()
#
#     one_way_button = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div["
#                                                    "2]/div/div/section/div[4]/div[1]/div["
#                                                    "3]/eol-datefield/eol-calendar/div/div/div[1]/div/label[2]/input")
#     driver.execute_script("arguments[0].click();", one_way_button)
#     sleep(2)
#     # wait.until(ec.element_to_be_clickable(driver.find_element(
#     #     By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/section/"
#     #               "div[4]/div[1]/div[3]/eol-datefield/eol-calendar/div/div/div[1]/"
#     #               "div/label[2]/input"))).click()
#
#     print("choose date")
#     current_date = date.today()
#     search_date = current_date + datetime.timedelta(3)
#     search_date = convert_date_to_string(search_date)
#     print(search_date)
#
#     tds = driver.find_elements(By.TAG_NAME, "td")
#     for td in tds:
#         if td.get_attribute("data-string") == search_date:
#             print("find search date")
#             button = td.find_element(By.TAG_NAME, 'a')
#             driver.execute_script("arguments[0].click();", button)
#             sleep(2)
#             # wait.until(ec.element_to_be_clickable(td.find_element(By.TAG_NAME, 'a'))).click()
#             break
#
#     print("close date selection")
#     button = driver.find_element(By.CSS_SELECTOR, "div[class = 'widget js-widget']")
#     driver.execute_script("arguments[0].click();", button)
#     sleep(1)
#     # wait.until(ec.element_to_be_clickable(
#     #     driver.find_element(By.CSS_SELECTOR, "div[class = 'widget js-widget']"))).click()
#
#     # search button
#     button = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[1]/div[2]/div/div/"
#                                            "section/div[4]/div[2]/div[3]/form/button")
#     driver.execute_script("arguments[0].click();", button)
#     sleep(30)
#
#     flight_elements = driver.find_element(By.CSS_SELECTOR, "div[class = 'ts-fbr-flight-list__body']")\
#         .find_elements(By.ID, "ctl00_c_FlightResultOutBound_rptBoundResult_ctl00_dvFltList")
#
#     print("flights founded")
#     flights = []
#     for flight_element in flight_elements:
#         e = flight_element.find_element(By.CSS_SELECTOR, "div[class = 'ts-fie__place']")
#         beginning = e.find_elements(By.TAG_NAME, 'span')[0].text
#         departure_time = e.find_element(By.ID, "ctl00_c_FlightResultOutBound_rptBoundResult_ctl00_timeDepart").text
#
#         e = flight_element.find_element(By.CSS_SELECTOR, "div[class = 'ts-fie__place ts-fie__right-side']")
#         destination = e.find_elements(By.TAG_NAME, 'span')[-1].text
#         arrival_time = e.find_element(By.ID, 'ctl00_c_FlightResultOutBound_rptBoundResult_ctl01_timeArrival').text
#
#         e = flight_element.find_element(By.CSS_SELECTOR, "div[class = 'ts-fie__infographic']")
#         duration = e.find_elements(By.TAG_NAME, 'span')[-1].text
#
#         connection_button = driver.find_element(By.ID, "ctl00_c_FlightResultOutBound_rptBoundResult"
#                                                        "_ctl00_aFlightDetails")
#         driver.execute_script("arguments[0].click();", connection_button)
#         sleep(2)
#         div = driver.find_element(By.CSS_SELECTOR, "div[class = 'ts-fie__place ts-fie__right-side']")
#         stop_place = div.find_elements(By.TAG_NAME, 'span')[-1].text
#         div = driver.find_element(By.ID, "ctl00_c_FlightResultOutBound_rptBoundResult_ctl00"
#                                          "_ctrlFlightModalContainer_ctl01_dvConnection")
#         stop_duration = div.find_element(By.TAG_NAME, 'p').find_element(By.TAG_NAME, "strong").text
#
#         close_button = driver.find_element(By.XPATH, "/html/body/form[1]/div[3]/div[3]/div[9]/div/div[14]/div["
#                                                      "2]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div["
#                                                      "2]/div/div/div[2]/button")
#         driver.execute_script("arguments[0].click();", close_button)
#         sleep(2)
#
#         e = flight_element.find_element(By.CSS_SELECTOR, "div[class = 'ts-fbr-flight-list-row__header-col"
#                                                          " RPA ts-fbr-flight-list-row__options ts-fbr-flight-"
#                                                          "list-row__options--3']")
#         e2 = e.find_element(By.CSS_SELECTOR, "div[class = 'ts-fbr-option ts-fbr-option--3 ts-fbr-option"
#                                              "--economy fbclass-y upgeconomy']")
#         flight_class = e2.find_element(By.CLASS_NAME, "ts-fbr-option__class").text
#
#         e = flight_element.find_element(By.CSS_SELECTOR, "div[class = 'ts-fbr-option__container']")
#         price = e.find_element(By.CLASS_NAME, "ts-fbr-option__price").text
#
#         flights.append(flight.Flight(beginning, destination, flight_date, arrival_time, departure_time,
#                                      price, flight_class, None, duration, stop_place, stop_duration))
#
#
# def convert_date_to_string(search_date):
#     day = int(search_date.day)
#     month = int(search_date.month) - 1
#     year = int(search_date.year)
#     return str(day) + str(month) + str(year)
