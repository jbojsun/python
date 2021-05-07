#면적 구하는 프로그램 using function
#filename : area.py

def cirArea(r):
    return 3.14159*r*r
def rectArea(b,h):
    return b*h
def triArea(b,h):
    return (1/2)*b*h

while True:
    print("0.끝내기")
    print("1.원의 면적 구하기")
    print("2.사각형의 면적 구하기")
    print("3.삼각형의 면적 구하기")
    choice = int(input("원하는 작업을 선택하세요:"))

    if choice == 0:
        break
    elif choice == 1:
        rad = int(input("원의 반지름 입력:"))
        print("반지름이",rad,"인 원의 면적은",cirArea(rad),"입니다.")
    elif choice == 2:
        base = int(input("밑변입력:"))
        height = int(input("높이입력:"))        
        print("밑변높이",base,height,"인 사각형의 면적은",rectArea(base,height),"입니다.")
    elif choice == 3:
        base = int(input("밑변입력:"))
        height = int(input("높이입력:"))        
        print("밑변높이",base,height,"인 삼각형의 면적은",triArea(base,height),"입니다.")
    else:
        print("잘못입력하셨습니다.")
print("작업을 마쳤습니다.")
    
