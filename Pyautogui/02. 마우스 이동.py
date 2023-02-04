import pyautogui as pygui

pygui.moveTo(100,100, duration = 1) # 얘는 절대좌표,, move는 상대좌표임

print(pygui.position()[0], pygui.position()[1])

