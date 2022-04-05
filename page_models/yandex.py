import os
from base.elements import WebElement, ManyWebElements
from base.pages import WebPage


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):

        if not url:
            url = os.getenv("MAIN_URL") or 'https://yandex.ru/'

        super().__init__(web_driver, url)

    search = WebElement(id='text')

    search_run_button = WebElement(xpath='//button[@type="submit"]')

    suggest_list = ManyWebElements(xpath="//ul[contains(@id, 'suggest-list')]/li")

    search_result_links = ManyWebElements(xpath="//ul[@id='search-result']/li/div[1]/div[2]/div[1]/a[1]")

    images_link = WebElement(xpath="//a[@data-id='images']")

    images_first_category = WebElement(xpath='//div[@class="PopularRequestList"]/div[1]/a')

    search_in_images = WebElement(xpath="//input[@name='text']")

    input_value = WebElement(xpath="//input[contains(@class, 'input__control')]")

    firs_image = WebElement(xpath="//a[contains(@class, 'serp-item')][1]")

    viewed_image_preview = WebElement(xpath="//img[@class='MMImage-Preview']")

    viewed_image_origin = WebElement(xpath="//img[@class='MMImage-Origin']")

    img_button_next = WebElement(xpath="//div[contains(@class, 'CircleButton_type_next')]")

    img_button_prew = WebElement(xpath="//div[contains(@class, 'CircleButton_type_prev')]")



