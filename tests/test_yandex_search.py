from page_models.yandex import MainPage


def test_check_search(web_browser):
    """ Search test """
    page = MainPage(web_browser)

    assert page.search.is_visible(), 'unseen search input '

    page.search = 'тензор'

    assert page.suggest_list.count() > 0, 'suggest list is empty'

    page.search.push_enter()

    for num, link in enumerate(page.search_result_links[:5]):
        assert 'tensor.ru' in link.get_attribute('href'), f"link № {num + 1} leads on {link.get_attribute('href')}"


def test_check_images(web_browser):
    """ Images test"""
    page = MainPage(web_browser)

    assert page.images_link.is_visible(), 'unseen images link'

    page.images_link.click()

    page.switch_to_window(page.window_handles()[1])

    assert page.get_current_url().split('?')[0] == 'https://yandex.ru/images/', f'incorrect redirect  from main ' \
                                                                                f'search on ' \
                                                                                f'{page.get_current_url()}'

    first_category_name = page.images_first_category.get_text()

    page.images_first_category.click()

    assert first_category_name == page.input_value.get_attribute('value'), 'incorrect image category redirect'

    page.firs_image.click()

    assert page.viewed_image_preview.is_visible(), 'image unopened'

    first_img_src = page.viewed_image_origin.get_attribute('src')

    page.img_button_next.click()

    second_img_src = page.viewed_image_origin.get_attribute('src')

    assert first_img_src != second_img_src, 'incorrect work of image next button'

    page.img_button_prew.click()

    last_img_src = page.viewed_image_origin.get_attribute('src')

    assert first_img_src == last_img_src, 'incorrect work of image previous button'

