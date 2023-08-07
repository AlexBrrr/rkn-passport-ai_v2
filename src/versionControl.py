import cv2


def testVersionCV2():
    if cv2.version.opencv_version == '4.5.5.64':
        print(f'Ok. opencv-python version is {cv2.version.opencv_version}')
    else:
        print(f'ERROR: opencv-python version is {cv2.version.opencv_version}'
              f'write in console "pip install opencv-python==4.5.5.64')


if __name__ == '__main__':
    testVersionCV2()
