import pyautogui as pygui
import cv2

icon = pygui.locateOnScreen("chemsketchicon.png", confidence = 0.7) #region = (x, y, wid, hei) )
print(icon)

if icon:
    print("오예")
else:
    print("아아")


while icon is None:
    icon = pygui.locateOnScreen("chemsketchicon.png", confidence=0.7)
    print("실패")

icon.click()
