#filename : printAddName.py
def prtAddName(name):           #function define with parameter
    print("부산시 연제구 연산동 고분로 170")        
    print("멀티미디어관 205호")
    print("{0} {1} {2}님".format(1,name,name))
    #print(name,"님")    #print("%s님" %name)

prtAddName("홍길동")           #call with argument(인수,인자)
prtAddName("이순신")
prtAddName("강감찬")
