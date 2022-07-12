from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import kayak_scrapper


def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         f'like Gecko) Chrome/79.0.3945.79 Safari/537.36')

    # s = Service(GeckoDriverManager().install())
    # driver = webdriver.Firefox(service=s)

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.delete_all_cookies()
    flights_list = kayak_scrapper.kayak_scrapper(driver)


if __name__ == '__main__':
    main()
