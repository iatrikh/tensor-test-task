from poms.sbis.sbis_home_pom import SbisHome


def test_case_1(chrome_driver):

    sbis_page = SbisHome.open_sbis_home(chrome_driver)
    sbis_contacts_page = sbis_page.open_contacts_page()
    tensor_home_page = sbis_contacts_page.find_and_click_tensor_banner()

    # Проверяем, что после клика по баннеру перешли на "https://tensor.ru/"
    assert (
        chrome_driver.current_url == "https://tensor.ru/"
    ), "Failed to open 'https://tensor.ru/'"

    ##

    people_block = tensor_home_page.find_people_block()

    # Проверяем блок "Сила в людях"
    assert (
        people_block.text == "Сила в людях"
    ), "Page https://tensor.ru/ does not contain 'Cила в людях' block"

    ##

    tensor_about_page = tensor_home_page.find_and_open_about()

    # Проверяем, что открылась страница "https://tensor.ru/about"
    assert (
        chrome_driver.current_url == "https://tensor.ru/about"
    ), 'Wrong page opened. Expected "https://tensor.ru/about"'

    ##

    images = tensor_about_page.find_images_in_rabotayem_block()

    firstImgWidth = images[0].get_attribute("width")
    firstImgHeight = images[0].get_attribute("height")

    # Проверяем, что все фото в разделе "Работаем" имееют одну и ту же ширину и высоту
    for img in images:
        assert (
            img.get_attribute("width") == firstImgWidth
        ), "Images have different width"
        assert (
            img.get_attribute("height") == firstImgHeight
        ), "Images have different height"
