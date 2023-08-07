import PIL.Image
import cv2
import numpy
import numpy as np
import pytesseract
from PIL import Image
from sys import platform
from config import TESSERACTPATH

if platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = TESSERACTPATH


def getImage(name: str) -> numpy.ndarray:
    """

    Преобразует входное изображение в многородный массив

    :param name: название изображения без .расширение
    :return: многородный массив изображения

    """
    return cv2.imread(f'images/{name}.jpg')


def getScreen(name: str) -> numpy.ndarray:
    """

    Преобразует входное изображение из screenshots в многородный массив

    :param name: название изображения без .расширение
    :return: многородный массив изображения. В дальнейшем "изображение"

    """
    return cv2.imread(f'screenshots/{name}.jpg')


def getGrayImg(img: numpy.ndarray) -> numpy.ndarray:
    """

    Преобразует входное изображение в черно-белое

    :param img: входное изображение (массив)
    :return: черно-белое изображение
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def getThreshholdImg(*, img: numpy.ndarray, thresh_lvl: int = 0) -> numpy.ndarray:
    """

    Яркость цвета определяется в диапазоне 0-255
        Форматирует входное изображение таким образом, что
            все пиксели от 0 до thresh_lvl становятся равны 0
            все пиксели от thresh_lvl до 255 становятся равны 255

    :param img: входное изображение
    :param thresh_lvl: пороговое значение
    :return: черно-белое изображение

    """
    return cv2.threshold(img, thresh_lvl, 255, cv2.THRESH_BINARY)[1]


def getResizeImage(*, img: numpy.ndarray, scale: int = 100) -> numpy.ndarray:
    """

    Изменяет размер входного изображение в соответствии со scale

    :param img: входное изображение
    :param scale: процент изменения изображение
    :return: измененное ( увеличенное / уменьшенное ) изображение

    """
    width: int = int(img.shape[1] * scale / 100)
    height: int = int(img.shape[0] * scale / 100)
    return cv2.resize(img, dsize=(width, height))


def getErodeImg(*, img: numpy.ndarray, scale: int = 3) -> numpy.ndarray:
    """

    Размывает входное изображение в соответствии со scale

    :param img: входное изображение
    :param scale: сила размытия
    :return: размытое изображение

    """
    return cv2.erode(img, np.ones((scale, scale), np.uint8), iterations=1)


def getContoursImage(*, input_img: numpy.ndarray, to_img: numpy.ndarray, wh_filter: list) -> list:
    """

    Находит контуры объектов на изображении
    Рисует контуры объектов на копии второго входного изображения

    :param input_img: входное изображение
    :param to_img: выходное изображение для контуров
    :param wh_filter: [ widht, height] фильтр ширины и высоты контура
    :return: [список контуров, выходное изображение с нарисованными контурами ]

    """
    contoursList: list = []
    outImg = to_img.copy()
    contours, hierarchy = cv2.findContours(input_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for idx, contour in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(contour)
        if w > wh_filter[0] and h > wh_filter[1]:
            if (w / h) > 1:
                cv2.rectangle(outImg, (x, y), (x + w, y + h), (255, 0, 0), 3)
                contoursList.append((x, y, w, h))
    contoursList.sort(key=lambda yCord: yCord[1], reverse=True)
    return [contoursList, outImg]


def getCropContourImage(*, contour: tuple, img: numpy.ndarray) -> numpy.ndarray:
    """

    Обрезает входное изображение до заданного контура
        img[y1:y2, x1:x2]

    :param contour: контур [x, y, w, h]
    :param img: входное изображение
    :return: Обрезанное изображение

    """
    x: int = contour[0]
    y: int = contour[1]
    w: int = contour[2]
    h: int = contour[3]
    return img[y:y + h, x:x + w]


def getLettersContour(*, input_img: numpy.ndarray, to_img: numpy.ndarray, wh_filter: list) -> list:
    """

    Находит контуры объектов на изображении
    Рисует контуры объектов на копии второго входного изображения

    Контуры находятся в соответствии с иерархией

    :param input_img: входное изображение
    :param to_img: входное изображение для контуров
    :param wh_filter: [ widht, height] фильтр ширины и высоты контура
    :return: [список контуров, выходное изображение с нарисованными контурами ]

    """
    contoursList: list = []
    outImg: numpy.ndarray = to_img.copy()
    contours, hierarchy = cv2.findContours(input_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for idx, contour in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(contour)
        if hierarchy[0][idx][3] == 0:
            if w > wh_filter[0] and h > wh_filter[1]:
                cv2.rectangle(outImg, (x, y), (x + w, y + h), (255, 0, 0), 3)
                contoursList.append((x, y, w, h))
    contoursList.sort(key=lambda yCord: yCord[1], reverse=True)
    return [contoursList, outImg]


def saveImage(*, name, img):
    """

    :param name: название изображения
    :param img: изображение
    :return: сохраняет изображение в папку images/

    """
    cv2.imwrite(f'images/{name}.jpg', img)


def getStringFromImg(*, input_image: numpy.ndarray, lang: str) -> str:
    """

    Распознает текст с изображения

    :param input_image: входное изображение
    :param lang: язык распознавания текста
    :return: распознанный и изображения текст
    """
    Pimg: PIL.Image.Image = getPILimage(cv_image=input_image)
    return pytesseract.image_to_string(Pimg, lang=lang)


def getPILimage(*, cv_image: numpy.ndarray) -> PIL.Image.Image:
    """

    Преобразует входное изображение ndarray в PIL формат

    :param cv_image: входное изображение ndarray
    :return: PIL.image.image

    """
    convertedImage: numpy.ndarray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(convertedImage)


def getFormatImages(*, inputImg, upscale: int, threshlvl: int, erodescale: int) -> list:
    """

    Обобщенная функция форматирования изображения

    :param inputImg: входное изображение
    :param upscale: процент изменения изображение
    :param threshlvl: пороговое значение
    :param erodescale: сила размытия
    :return: [ Изображение с измененным размером, Черно-белое изображение,
                Черно-белое контрастное изображение, Размытое изображение ]
    """
    pasportImgUpScale: numpy.ndarray = getResizeImage(img=inputImg, scale=upscale)
    pasportImgGray: numpy.ndarray = getGrayImg(img=pasportImgUpScale)
    pasportImgThresh: numpy.ndarray = getThreshholdImg(img=pasportImgGray, thresh_lvl=threshlvl)
    pasportImgErode: numpy.ndarray = getErodeImg(img=pasportImgThresh, scale=erodescale)
    return [pasportImgUpScale, pasportImgGray, pasportImgThresh, pasportImgErode]
