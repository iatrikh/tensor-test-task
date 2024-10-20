from poms.sbis.sbis_home_pom import SbisHome


def test_case_2(chrome_driver):

    sbis_page = SbisHome.open_sbis_home(chrome_driver)
    sbis_contacts_page = sbis_page.open_contacts_page()

    expected_current_region = "Свердловская обл."

    region = sbis_contacts_page.find_current_region()

    # Проверяем, что автоматический определился регион пользователя

    assert (
        region.text == expected_current_region
    ), f"Wrong region displayed. Expected: '{expected_current_region}'"

    ##

    partners_by_city = sbis_contacts_page.find_parters_block()

    # Проверяем, что отобразился список партнеров в регионе
    assert partners_by_city.is_displayed(), "Partners list not found"

    ##
    new_region = "Камчатский край"
    sbis_contacts_page.change_region_to(new_region)

    region = sbis_contacts_page.find_current_region()

    # Проверяем, что отображается новый выбранный регион
    assert (
        region.text == new_region
    ), f"Wrong region displayed. Expected: '{new_region}'"

    ##

    partners_by_city = sbis_contacts_page.find_parters_block()

    # Проверяем, что отображается новый список партнеров
    assert (
        partners_by_city.text == "Петропавловск-Камчатский"
    ), "Expected city in partners list: 'Петропавловск-Камчатский'"

    ##
    # Проверяем, что url сожержит информацию выбранного региона
    assert "41-kamchatskij-kraj" in chrome_driver.current_url

    ##
    # Проверяем, что title сожержит информацию выбранного региона
    assert "Камчатский край" in chrome_driver.title
