import pyautogui as pygui
import cv2
#01. .5초간 기다린다.
pygui.sleep(0.5)


#2. 켐스케치 버튼을 누른다.
icon_chemsketch = pygui.locateOnScreen("chemsketchicon.png", confidence = 0.7, region = (168,1027,1452-168,1078-1027)) #region = (x, y, wid, hei) )
print(icon_chemsketch)
pygui.click(icon_chemsketch)
print("켐스케치를 실행합니다.")
pygui.sleep(3)

#3. 화면창에서 ok버튼을 누른다.
icon_chemsketchokbutton = pygui.locateOnScreen("chemsketch_okbutton.png", confidence=0.96)
while icon_chemsketchokbutton is None:
    icon_chemsketchokbutton = pygui.locateOnScreen("chemsketch_okbutton.png", confidence=0.96)
    print("시ㄹ패")
pygui.click(icon_chemsketchokbutton)
print("빈 화면이 나타납ㅂ니다.")
pygui.sleep(2)

#4. 전체화면을 만든다.
icon_fullscreenwindowbutton = pygui.locateOnScreen("chemsketch_fullscreenwindowbutton.png", confidence=0.99)
icon_nonfullscreenwindowbutton = pygui.locateOnScreen("chemsketch_nonfullscreenwindowbutton.png", confidence=0.99)
if icon_fullscreenwindowbutton is None:
    pygui.click(icon_nonfullscreenwindowbutton)
else:
    pass
pygui.sleep(2)
#5. generate_smile까지 도달하기

icon_toolsbutton = pygui.locateOnScreen("chemsketch_toolsbutton.png", confidence=0.99)
pygui.click(icon_toolsbutton)
print("tools를 눌렀읍니다.")
pygui.sleep(0.05)

icon_generatebutton = pygui.locateOnScreen("chemsketch_generatebutton.png", confidence=0.99)
pygui.click(icon_generatebutton)
print("generate를 눌렀읍니다.")
pygui.sleep(0.05)

icon_formsmilebutton = pygui.locateOnScreen("chemsketch_fromsmilebutton.png", confidence=0.99)
pygui.click(icon_formsmilebutton)
print("smile로 만들기 창으로 진입합니다.")
pygui.sleep(1)

#6. 입력창에 smile을 입력합니다.
smilewindow = pygui.getActiveWindow()
smilewindow.activate()
pygui.sleep(0.1)
pygui.write("aaaas@@[s]s", interval = 0.07)








# 168,1027 140,101,18 #8C6512
#1452,1078 127,94,21 #7F5E15