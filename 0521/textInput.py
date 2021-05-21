import turtle as t
t.shape('turtle')
t.clear()

s = t.textinput("Name Box","이름을 입력해주세요.")
t.write("안녕하세요 "+s+"님 반갑습니다.")

for i in range(4):
    t.forward(200)
    t.left(90)
    
