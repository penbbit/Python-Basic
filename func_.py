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