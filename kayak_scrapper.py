from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import flight
import datetime


def kayak_scrapper(driver):
    url = "https://www.kayak.com/flights/AMS-IKA/2022-03-01?sort=bestflight_a"
    driver.get(url)
    sleep(3)

    e = driver.find_element(By.CSS_SELECTOR, "div[class = 'listInner']"). \
        find_element(By.CSS_SELECTOR, "div[class = 'Base-Results-ResultsList Flights-Results-FlightResultsList']")

    # flight_elements = e.find_elements(By.CSS_SELECTOR, '#KBHCX-u641-1 > div')
    flight_elements = e.find_elements(By.CSS_SELECTOR, "div[class = 'resultWrapper']")
    for a in flight_elements:
        print(a)

    flight_date = None
    try:
        temp = driver.find_element(By.CSS_SELECTOR, "div[class = 'lNCO lNCO-mod-pres-default "
                                                    "lNCO-mod-spacing-medium lNCO-mod-size-large "
                                                    "lNCO-mod-opened']") \
            .find_element(By.CSS_SELECTOR, "span[class = 'PDPe-from-date']").text
        flight_date = convert_date(temp)
    except NoSuchElementException:
        print("can not find date")

    beginning = None
    destination = None
    try:
        e = driver.find_element(By.CSS_SELECTOR, "div[class = 'zEiP-formContainer']")
        beginning = e.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div/div/div/"
                                             "div[1]/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div[1]").text
        beginning = beginning[:-6]
        destination = e.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div/div/"
                                               "div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div/"
                                               "div[1]").text
        destination = destination[:-6]
    except NoSuchElementException:
        print("can not find beginning and destination")

    flights = []
    for flight_element in flight_elements:
        try:
            print("in looooooooooooop")
            flight_class = None
            capacity = None
            e = flight_element.find_element(By.CSS_SELECTOR, "div[class = 'resultInner']") \
                .find_element(By.CSS_SELECTOR, "div[class = 'Flights-Results-ResultInfo']") \
                .find_element(By.CSS_SELECTOR, "div[class = 'container']")

            times_e = e.find_element(By.CSS_SELECTOR, "div[class = 'section times']")
            temp = times_e.find_elements(By.CSS_SELECTOR, "span[class = 'time-pair']")
            departure_time = convert_time2(temp[0].text)
            arrival_time = convert_time2(temp[-1].text)
            airline = times_e.find_element(By.CSS_SELECTOR, "div[class = 'bottom ']").text

            stop_e = e.find_element(By.CSS_SELECTOR, "div[class = 'section stops']")
            stop_place = stop_e.find_element(By.CSS_SELECTOR, "span[class = 'js-layover']").text

            duration_e = e.find_element(By.CSS_SELECTOR, "div[class = 'section duration allow-multi-modal-icons']")
            duration = convert_time1(duration_e.find_element(By.CSS_SELECTOR, "div[class = 'top']").text)

            temp = duration_e.find_elements(By.CSS_SELECTOR, "div[class = 'bottom-airport']")
            beginning_airport = temp[0].find_element(By.CSS_SELECTOR, "span[class = 'airport-name']").text
            destination_airport = temp[-1].find_element(By.CSS_SELECTOR, "span[class = 'airport-name']").text

            price_e = flight_element.find_element(By.CSS_SELECTOR, "div[class = 'col-price result-column js-no-dtog']")
            price = price_e.find_element(By.CSS_SELECTOR, "span[class = 'price-text']").text
            # delete $ from string and convert it to float
            price = float(price[1:])
            try:
                temp = price_e.find_element(By.CSS_SELECTOR, "div[class = 'Common-Booking-MultiBookProvider "
                                                             "Theme-featured-name-only featured-provider cheapest "
                                                             "multi-row']"). \
                    find_element(By.CSS_SELECTOR, "span[class = 'name-only-text']").text
                arr = str(temp).split(" ")
                for a in arr:
                    if a.isdigit():
                        capacity = int(a)
                        break
            except NoSuchElementException:
                print("can not find capacity")
            # details
            try:
                button = flight_element.find_element(By.CSS_SELECTOR, "div[class = 'inner-grid keel-grid']")
                driver.execute_script("arguments[0].click();", button)
                sleep(10)

                try:
                    flight_class = flight_element.find_elements(By.CSS_SELECTOR,
                                                                "div[class = 'dErF-cabin-class js-farename']")[0].text
                except IndexError:
                    print("can not find class")
            except Exception:
                pass

            flights.append(flight.Flight(beginning, beginning_airport, destination_airport, destination,
                                         flight_date, arrival_time, departure_time, price, flight_class, capacity,
                                         airline, duration, stop_place, stop_duration=None))
        except Exception:
            continue
    return flights


def convert_date(date_string):
    arr = str(date_string).split("/")
    flight_date = datetime.date(int(arr[2]), int(arr[0]), int(arr[1]))
    return flight_date


# pattern: "xh ym"
def convert_time1(time_string):
    arr = str(time_string).split(" ")
    h = arr[0]
    h = int(h[:-1])
    m = arr[1]
    m = int(m[:-1])
    return datetime.time(h, m)


# pattern = "x:y pm/am"
def convert_time2(time_string):
    arr = str(time_string).split(" ")
    arr2 = arr[0].split(":")
    h = int(arr2[0])
    m = int(arr2[1])
    if arr[1] == "am":
        if h == 12:
            h = 00
    else:  # pm
        if h != 12:
            h = h + 12
    return datetime.time(h, m)
