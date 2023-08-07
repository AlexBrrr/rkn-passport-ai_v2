import random
from config import URL
from html2image import Html2Image


def getScreenshot():
    """

    Делает скриншот страницы браузера по URL
        и сохраняет в screenshots/ в формате .jpg

    :return:

    """
    randomNum = random.randint(0, 999_999_999)
    hti = Html2Image()
    hti.output_path = 'screenshots/'
    hti.screenshot(url=URL, save_as=f'{randomNum}.jpg')

