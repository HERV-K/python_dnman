
btnname = input("버튼 이름")
btnwin = input("버튼 넣을 창")
btntext = input("버튼 텍스트")
btnposition = input("row, col")
print(btnposition)


print(f"{btnname} = Button({btnwin}, text = {btntext})")
print(int(btnposition[0, int(btnposition.rfind(','))-1]))
print(f"{btnname}.grid(row = {int(btnposition[0, int(btnposition.rfind(','))-1])}, column = {int(btnposition[int(btnposition.rfind(','))+1:])})")