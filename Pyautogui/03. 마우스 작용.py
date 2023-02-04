import pyautogui as pygui
print("시작")
pygui.sleep(3)
print("기다림은 끝났다.")
print(pygui.position()[0], pygui.position()[1])
pygui.click(73, 33, duration = 1)

pygui.click(clicks = 10)

pygui.rightClick()
pygui.middleClick() # 휠 클릭

pygui.mouseDown()
pygui.sleep(0.1)
pygui.mouseUp()



pygui.drag(100,0, duration=0.1)

