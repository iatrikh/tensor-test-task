import os
from poms.sbis.sbis_home_pom import SbisHome


def test_case_3(chrome_driver):

    sbis_page = SbisHome.open_sbis_home(chrome_driver)
    download_page = sbis_page.open_local_versions()

    download_page.find_and_download_win_plugin()

    # Формально проверяем наличие скачанного файла.
    assert os.path.exists(
        "downloads\\sbisplugin-setup-web.exe"
    ), "Expected file 'sbisplugin-setup-web.exe' not found"

    ##

    file_size = os.path.getsize("downloads\\sbisplugin-setup-web.exe") / 1024**2

    # У файла теперь другой размер, отличающийся от привиденного в задании.
    assert (
        round(file_size, 2) == 11.46
    ), f"Expected file size: 11.46, but got: {round(file_size, 2)}"

    # Удаляем скачанный файл, чтобы можно было запустить тест повторно
    if os.path.exists("downloads\\sbisplugin-setup-web.exe"):
        os.remove("downloads\\sbisplugin-setup-web.exe")
