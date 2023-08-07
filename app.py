from src.imageControl import getScreen, getFormatImages, getContoursImage, \
    getCropContourImage, getStringFromImg, saveImage


def getPasportLinesData(*, pasportName: str):
    pasportImg = getScreen(pasportName)
    pasportImgFormat = getFormatImages(inputImg=pasportImg, upscale=200, threshlvl=100, erodescale=25)
    pasportLineContours = getContoursImage(
        input_img=pasportImgFormat[3],
        to_img=pasportImgFormat[0],
        wh_filter=[800, 10]
    )

    saveImage(name='pasport', img=pasportImgFormat[0])
    saveImage(name='contours', img=pasportLineContours[1])

    twoLinesText: list[str] = []
    for contour in pasportLineContours[0]:
        line = getCropContourImage(contour=contour, img=pasportImgFormat[0])
        lineFormat = getFormatImages(inputImg=line, upscale=200, threshlvl=100, erodescale=10)
        textFromImg = str(getStringFromImg(input_image=lineFormat[2], lang='eng')).replace(' ', '')
        twoLinesText.append(textFromImg)
    return twoLinesText


def main():
    linesData = getPasportLinesData(pasportName='690757')
    firstLine, secondLine = linesData[1], linesData[0]
    print(f'Первая строка: {firstLine}Вторая строка: {secondLine}')


if __name__ == '__main__':
    main()
