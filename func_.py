# 함수(function)
# 함수란 어떤 기능을  하는 것으로 크게 이미 있는것과 직접 만든 함수가 있다.



# def function_name(parameter):
#     codes...
#     return value[variable]

# 위형식으로 함수를 직접 만들 수 있으며 만든 함수 실행의 경우 아래와 같음
# function_name(argument)

# parameter : 함수 내부에서 사용하는 변수
# return    : 함수로 종료하여, 특정 값을 함수를 실행한 곳으로 돌려줄 수 있음
# argument  : 함수를 실행할때  넘겨주는 값
# parameter argument return는 필수가아님
# 함수를 정의할 때 parameter의 개수와 함수를 실행할때의 argument 의 개수는 같아야 함.


# def a():
#     print("Hello")

# def b(name):
#     print(name,"Hi")

# def c(a):
#     return a+10

# a()
# b("Jeong")
# var = c(5)
# print(var)
# b(var)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# def welcome(name):
#     print('Hello!',name)
#     return 'bye'

# print(welcome("영준"))


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# def say(name):
#     print(name,"님이 입장하셨습니다.")

# say("park")
# say("kim")
# say("choi")
# say("yang")
# say("lee")
# say("gang")
# say("jo")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# return의 경우 보통 함수끼리 값을 공유할 때 사용

# def check_score(score):     #점수들 중 50점이상의 점수를 구분하여 리스트로 리턴
#     over = []
#     for i in score:
#           if(i >= 50):
#             over.append(i)

#     return over

# def average(score):     #평균을 구함
#     print(sum(score) / len(score))


# score = [51, 99, 78, 34, 75, 22, 12]
# over_50 = check_score(score)    #check_score 함수를 통해서 50점 이상인 점수를 over_50 변수에 저장
# print(over_50)
# average(over_50)                #50 점이상인 점수의 평균을 구함


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# def star(x):
#    print('*'*x)

# for i in range(1,10,1):
#     star(i)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# def speed(d, t):
#     s = d/t
#     return s

# print(speed(10,10))


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# def area(b, h):
#     a = b*h/2
#     return a
# print(area(10,20))


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# def star(n):
#     print('*'+' '*n+'*'+' '*(5-n)+'*')

# for i in range(0,6,1):
#     star(i)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 변수는 크게 local,global 2가지가 있음
# local 변수  : 함수 내부에서 만들었고 함수 내부에서만 쓰이는 변수
# global 변수 : 함수 밖에서 만들었고 함수 내외부에서 둘다 사용 가능
# 변수의 이름과 local, global은 상관 없으며, 변수는 기본적으로 global 변수를 얘기함

# a = 10 #global 변수

# def test():
#     a =5    #local 변수
#     b = 20  #local 변수

# test()
# print(a)    #test 함수를 실행해도 a 변수의 값은 변화가 없음
# print(b)    #변수 b는 test 함수에서만 사용하기 떄문에 함수 밖에서 참조를 하는 경우 에러 발생


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 함수 밖에 있는 변수의 값을 한수 내부에서 변경하는 법
# global 변수
# 위 형식으로 함수 내부에서 함수 밖에 있는 변수의 값을 변경할 수 있음
# global을 사용안해도 함수를 내부에서 값을 참조는 가능하지만 값 변경은 불가능

# bmi = 0                 #global 변수


# def BMI(height, weight):
#     global bmi                      #함수 내부에서 global 사용하여 값을 변경할 수 있음(이거 안쓰면 안댐)
#     #global bmi = 0                 #global 키워드에서 변수에 값을 넣을 수는 없음 (오류)

#     height = height/100
#     bmi = weight / (height * height)

#     return bmi

# print(bmi)
# print(BMI(178,80))              #BMI 함수에서 리턴된 값을 출력
# print(bmi)                      #BMI 함수에서 global 키워드를 이용하여 bmi 변수의 값을 변경함


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# 피보나치 수
# https://pythontutor.com

# def fibonacci(a,b):
#     c = a+b
#     if (a <100):
#         print(a,end=' ')
#         return fibonacci(b,c)   #return None이 계속 반복되면서 호출된 함수들이 종료된다.
#     else:                      
#         return                   #return 하는 값 또는 변수가 없기 떄문에 None이 return 됨
    
# fibonacci(1,1)
# print()


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# def star(n):
#     b = 2**(n-1)
#     if(b<17):
#         print('*'*b, end=' ')
#         star(n +1)
#     else:
#         return
    
# star(1)
# print()


# def star(n):
#     sum = n+n
#     if(n <= 16):
#         print('*'*n,end=' ')
#         return star(sum)
#     else:
#         return
# star(1)
# print()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# def at(a,b):
#     if(b<9):
#         print('@'*a+'^'*b, end=' ')
#         c = a*b
#         at(b,c)
#     else:
#         return
    
# at(1,2)
# print()



# def at (a,b):
#     c=b
#     d=a * b
#     if(a <= 4):
#         print('@'*a,end='')
#         print('^'*b,end='')
#         return at(c,d)
#     else:
#         return
# at(1,2)
# print()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#