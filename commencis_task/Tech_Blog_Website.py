from selenium import webdriver
import logging

aaa
#Direction of webdriver has designated
driver = webdriver.Chrome(executable_path=r'D:\Automation\selenium\chromedriver.exe')

#Log file created and format designated
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='logs.txt', level=logging.INFO)
logger = logging.getLogger()

#Website that we are going to work on has opened
driver.get(r'https://techcrunch.com/')
driver.maximize_window()

class News_Content:
    def check_author(counter,title):
        author = f"//div[@class='river river--homepage ']/div[1]/article[{counter}]/header[1]/div[1]/div[1]/span[1]/span[1]"
        if len(author) > 0:
            logger.info(f"Author of '{title}' news is exist")
        else:
            logger.info(f"There is no author for '{title}'. Please check!")
    def check_images(counter,title):
        image = f"//div[@class='river river--homepage ']/div[1]/article[{counter}]/footer[1]/figure[1]/picture[1]/img[1]"
        if len(image) > 0:
            logger.info(f"Image of the '{title}' news is exist")
        else:
            logger.info(f"There is no image for '{title}' news. Please check!")
    def compare_titles(counter):
        # I will compare last news title
        title = driver.find_element_by_xpath(
            f"//div[@class='river river--homepage ']/div[1]/article[{counter - 1}]/header[1]/h2[1]/a[1]").get_property('innerText')

        driver.find_element_by_xpath("//div[@class='river river--homepage ']/div[1]/article[1]").click()

        # Assigned title which is inside
        compared_title = driver.find_element_by_xpath("//h1[@class='article__title']").get_property('innerText')

        if compared_title == title:
            logger.info(
                f"Titles which is for news list and news itself are same for '{title}' news. Case is successfull")
        else:
            logger.info(f"Titles are not matching for '{title}' news")

#Counter for each news
counter = 1

#Checking cases for each news via this while loop
while 2 == 2:
    #We will check is there a news or not with the help of this variable
    a = driver.find_elements_by_xpath(f"//div[@class='river river--homepage ']/div[1]/article[{counter}]")

    #If the news exist execute tests and log
    if len(a) > 0:

        #News title
        title = driver.find_element_by_xpath(f"//div[@class='river river--homepage ']/div[1]/article[{counter}]/header[1]/h2[1]/a[1]").get_property('innerText')
        News_Content.check_author(counter, title)
        News_Content.check_images(counter, title)
        counter += 1
    else:
        logger.info(f"There are {counter - 1} news and Image and Authors has checked sucessfully.")
        News_Content.compare_titles(counter)
        break



