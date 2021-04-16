#filename : sum01

num = int(input("정수입력:"))
sum=0
for i in range(1,num+1):
    if i < num:
        print(i,"+",end="")
    else:
        print(i,"=",end="")
    sum += i

print(sum)


#end= 줄바꾸기 X
