# rkn-pasport-ai-v2

Для запуска приложения написать в консоль:

    python -m venv venv

⠀

    pip install requirements.txt
  
Запустить src.VersionControl.py, проверить версию opencv-python

Запустить backend.py, создать скриншоты паспорта

Указать в app.py название изображения, запустить    

src.imageControl.py - настройки изображения

src.pasportData.py - генерация данных паспорта

src.webScreenshot.py - скриншот страницы браузера

src.versionControl.py - проверка версии opencv-python

app.py - основной файл программы

backend.py - сайт для генерации изображений
    
    "/" - генератор
    
    "/show/" - выбрать изображение \ скриншоты сохраняются в screenshots, нужно скопировать в static/images
    
    "/show/ID" - показать выбранное изображение

config.py - основные настройки для backend.py

requirements.txt - файл с зависимостями

.env - файл со скрытыми данными. Должен содержать URL, SECRETKEY и если вы на windows -> путь до tesseract.exe

screenshots - сохраненные со страницы браузера изображения паспорта

images - сохраненные изображения конкретной генерации паспорта во время выполнения app.py
