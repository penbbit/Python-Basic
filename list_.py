# list.py

# 변수 = ['값' , 값 ]     => 값의 자료형은 상관 없음
# 위 형식으로 선언
# 리스트란 여러개의 자료형을 하나의 변수에 순서대로 모아둔 것
# 모아둔 자료형의 순서는 0부터 시작한다 => 인덱스(index) 번호라고 얘기
# 리스트의 값을 가지고 올때는 대괄호([])를 이용하여 참조

# list1 = [1, 'cit', True]
# print(list1)
# print(list1[0])
# print(list1[2])
# print(list1[3])


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 인덱스 번호를 이용해서 해당 인덱스 번호에 있는 값을 수정할 수 있다.
# 값 변경은 변수에 값을 저장하는 것처럼 진행하면 된다.
# list1 = [1, 'cit', True]
# print(list1)

# list1[1] = 'hello' list1의 1번째 인덱스의 값을 변경
# print(list)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# list1 = ['abc', 'dfg', 'hij', 123, 456]
# print(list1)
# print()

# print("Q1.list1의 첫번째 원소를 'park' 로 고치시오")
# list1[1] = 'park'
# print(list1)
# print()

# print("Q2. 변수 이름을 'arr'로 하고 아래 리스트를 대입(저장)하시오, [4, 8, 12, 16, 20, 24, 28, 32]")
# arr = [4, 8, 12, 16, 20, 24, 28, 32]
# print(arr)
# print()

# print("Q3. arr의 4번째 원소를 'cit'로 하시오. 단 맨 왼쪽의 원소가 0번째 원소다.")
# arr[4] = 'cit'
# print(arr)
# print()

# print("Q4. print(list1) 와 print(arr)을 실행하시오.")
# print(list1)
# print(arr)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# test = ['test', 1, 8, 'hi', '3.15']

# for i in test:      기존에 배웠던 for문의 range 자리에 리스트를 넣어서
#                     리스트 내용을 전부 출력할 수 있음
#     print(i, end='')

# print()


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# name = ['지훈', '서준', '시찬','윤서']
# score = [92, 96, 98, 100]
# average = (score[0] + score[1] + score[2] + score[3])/4
# print("평균은", average,"이고",name[3],"가 점수가 가장 점수가 높습니다.")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 리스트 함수

# 리스트명.insert(인덱스 번호, 추가할 값)
# insert()함수는 인덱스 번호 위치에 값을 추가, 기존 위치에 있는 값은 뒤로 밀림
# 인덱스 번호가 리스트의 범위를 벗어나는 경우 값을 리스트 제일 뒤에 추가됨

# 리스트명.append(추가할 값)
# append() 함수는 리스트 제일 뒤에 값을 추가 

# del(리스트명[인덱스 번호])
# del()함수는 인덱스 번호에 해당하는 값을 리스트에서 삭제
# 만약 삭제한 위치 뒤에 값이 있으면 앞으로 당겨짐
# 인덱스 번호가 범위를 벘어나면 에러 발생 

# 리스트명.remove(삭제할 값)
# remove() 함수는 리스트에서 특정 값을 삭제
# 만약 삭제할 값이 여러개면 제일 앞에 있는 한개의 값만 삭제
# 만약 삭제할 값이 리스트에서 없으면 에러 발생

# 리스트명.index(인덱스 번호를 찯을 값)
# index()함수는 특정 값의 인덱스 번호를 알려줌
# 특정 값이 여러개면 가장 앞에 있는 인덱스 번호를 알려줌
# 값이 리스트에서 없을 경우 에러 발생

# len(리스트명)
# len()함수는 리스트의 크기(길이)를 알려줌

# sum(리스트명)
# sum()함수는 리스트의 값을 전부 더해줌, 리스트 내부의 값이 전부 숫자일 경우만 가능

# 리스트명.count(개수를 알고 싶을 값)
# count() 함수는 특정 값이 리스트에 몇개 있는지 알려줌
# 만약 특정 값이 리스트에 없으면 0

# 리스명.sort()
# sort()함수는 리스트이 내용을 오름차순으로 정렬

# insert()와 같이 리스트 변수와 .을 같이 사용하는 함순느 리스트에서만 사용 가능하고
# del(), len(), sum()의 경우는 리스트 말고도 다른 자료형에서도 사용가능


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# list0 = []
# print(list0)
# print()

# print("Q1.append를 사용해 list0에 1,2,3,4,5,6,7,8,9 를 차례로 추가시오.(반복문을 사용해도 좋다.)")
# for x in range(1,10,1):
#     list0.append(x)
# print(list0)
# print()

# print("Q2.insert함수를 사용해 list0의 0번째에 0을 추가하시오.")
# list0.insert(0,0)
# print(list0)
# print()

# print("Q3.del 함수를 이용해 list0의 3번쨰 원소를 삭제하시오.")
# del(list0[3])
# print(list0)
# print()

# print("Q4.del 함수를 이용해 list0의 5번째 원소를 삭제하시오.")
# del(list0[5])
# print(list0)
# print()

# print("Q5.remove 함수를 이용해 list0에서 1을 삭제하시오")
# list0.remove(1)
# print(list0)
# print()

# print("Q6.index 함수를 이용해 list0에서 5가 몇번째에 위치했는지 출력하시오.")
# print(list0.index(5))
# print()

# print("Q7.index 함수를 이용하여 list0에서 6이 존재하는지 확인하시오.몇번째에 이치해ㅆ는지 출력하시오.")
# try :
#     print(list0.index(6))
# except :
#     print("6이 없음")
# print()

# print("Q8.len 함수를 이용해 list0의 원소의 개수를 출력하시오.")
# print(len(list0))
# print()

# print("Q9.print(list0)을하여 리스트를 출력하시오.")
# print(list0)
# print()


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# week = ['Mon','Thu','Wed','Thu','Fri']
# print(week)
# print()

# print("Q1.'Sat'와'Sun'을 차례로 뒤에 추가하시오")
# week.append('Sat')
# week.append('Sun')
# print(week)
# print()

# print("Q2.첫번째 'Thu'를 지우고 그자리에 'Tue'를 삽입하시오.")
# del(week[1])
# week.insert(1,'Tue')
# print(week)
# print()

# print("Q3.'Wed'의 인덱스를 출력하시오")
# print(week.index('Wed'))
# print()

# print("Q4.week 리스트 변수의 원소의 개수를 출력하시오.")
# print(len(week))
# print()

# print("Q5.print(week)를 실행하시오.")
# print(week)
# print()


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# print("점수를 입력하세요.(끝낼 시 0을 입력)")
# nums = []                   # 리스트에 누적할려면 반복문 밖에 있어야함

# while(True):
#     num = int(input())
#     if(num==0):             # break를 먼저하면 리스트에 안들어가서 len-1을 안해도 됨
#         break

#     nums.append(num)

# avg = sum(nums)//(len(nums))
# print("평균은", avg, "입니다")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=+++++++++++++++++++++++#


# in
# in은 리스트에 해당 값이 있는지 없는지를 True,False로 알려줌, if에 주로 사용
# 찾을값 in 리스트명
# 위 형식으로 사용함

# numbers = [1, 2, 3, 4, 5]
# print(2 in numbers)
# print(8 in numbers)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 이중 리스트
# 하나의 리스트 내부에 또다른 리스트가 있는 경우
# 내부 리스트의 값을 참조할 때는 []를 2개 사용한다.

# list1 = [1, 'cit', True]
# list2 = [3, 2, 'py']
# list3 = [list1, list2]
# print(list1)
# print(list2)
# print(list3)
# print(list3[0][1])
# print(list3[1][1])
# print(list3[0])


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 삼중 리스트(3차원 리스트)
# 하나의 리스트 내부에 또다른 하나의 리스트 내부에 또다른 리스트가 있는것
# 값을 참조할 때 []를 3개 사용한다.


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# Cafe = ['Starlucks','Mollys','Emiya','FomAFams']
# Main = ['Americano','cappuccino','cafelatte','Americano']
# Price = [3700,4600,3200,4100]
# Location = ['Astreet','Bstreet','cafelatte', 'Americano']
# CafeTable = [Cafe,Main,Price,Location]
# print(CafeTable)
# print()

# 이중 리스트의 내용을 한줄씩 보기
# for i in CafeTable:
#     print(i)
# print()

# 가격의 정보만 출력
# print(CafeTable[2])
# print()

# Mollys의 정보만 출력
# for i in range(len(CafeTable)):
#     print(CafeTable[i][1], end=' ')
# print()


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# A = [1,4,5]
# B = [2,3,6]
# C = []

# for i in A:
#     for x in B:
#         C.append(i*x)
# for z in C:
#     print(z)