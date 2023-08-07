import random
import string
from pprint import pprint as pp


def printData(pasportdata):
    print(f'------ PASPORT DATA ------\n'
          f'{pp(pasportdata)}'
          f'--------------------------\n')


def getRandomPasportData() -> dict:
    """

    :return: рандомно сгенерированные паспортные данные

    """
    return {
        'issued': getRandomText(30).upper(),
        'issuedDate': f'{getRandomNum(10, 99)}.{getRandomNum(10, 99)}.{getRandomNum(1000, 9999)}',
        'divCode': f'{getRandomNum(100, 999)}-{getRandomNum(100, 999)}',
        'name': getRandomText(10).capitalize(),
        'surname': getRandomText(15).capitalize(),
        'patronymic': getRandomText(10).capitalize(),
        'gender': 'муж',
        'birthDay': f'{getRandomNum(10, 99)}.{getRandomNum(10, 99)}.{getRandomNum(1000, 9999)}',
        'city': getRandomText(10).capitalize(),
        'pasportSerial': f'{getRandomNum(10, 99)} {getRandomNum(10, 99)}',
        'pasportNumber': getRandomNum(100_000, 999_999),
        'firstLine': getPasportFirstLineCode(),
        'secondLine': getPasportSecondLineCode(),
    }


def getRandomPasportTransform() -> list:
    """

    В данный момент не используется
        skewX: int = getRandomNum(-20, 20)
        rotate: int = getRandomNum(-20, 20)
        scaleX: int = getRandomNum(-10, 20)

    :return: параметры редактирования взображение

    """
    skewX, rotate, scaleX = 0, 0, 0
    return [skewX, rotate, scaleX]


def getRandomText(letters: int) -> str:
    """

    Возвращает рандомно сгенерированный текст

    :param letters: количество букв в тексте
    :return: текст с рандомным набором букв

    """
    alphabet: str = 'абвгдежзийклмнопрстуфхцчшщыэюя    '
    return ''.join(random.choice(alphabet) for _ in range(letters))


def getRandomNum(from_value: int, to_value: int) -> int:
    """

    Возвращает рандомное число в заданном диапазоне

    :param from_value: начало диапазона
    :param to_value: конец диапазона
    :return: рандомное число

    """
    return random.randint(from_value, to_value)


def getPasportFirstLineCode() -> str:
    """

    :return: рандомно сгенерированная первая строка паспорта

    """
    letters: str = f'{string.ascii_lowercase}' + '<' * 50
    return ''.join(random.choice(letters) for _ in range(42))


def getPasportSecondLineCode() -> str:
    """

    :return: рандомно сгенерированная вторая строка паспорта

    """
    letters: str = f'{getRandomNum(111_111_111, 999_999_999)}' + '<' * 5
    return ''.join(random.choice(letters) for _ in range(42))
