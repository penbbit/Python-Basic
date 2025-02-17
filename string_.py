# string = "cit academy"

#인덱스 번호를 이용하여 문자열의 하나의 값을 가지고 올 수 있음
#print(string[3])
# print(string[6])

#슬라이싱을 이용하여 문자열의 일부분의 값을 가지고 올 수 있음
#print(string[1:4])  #string 변수의 문자열 인덱스의 1부터 4까지의 값을 가지고 옴(4는 미포함 x)
#print(string[5:9])  #string 변수의 문자열 인덱스의 5부터 9까지의 값을 가지고 옴(9는 미포함 x)

# 슬라이싱의 숫자를 생략할수 있음.
# 생략을 할 경우 처음 또는 끝까지 값을 가지고 옴
#print(string[:3])   #string 변수의 문자열 인덱스의 처음부터 3까지의 값을 가지고 옴(3은 미포함 x)
#print(string[8:])   #string 변수의 문자열 인덱스의 8부터 끝까지의 값을 가지고 옴
#print(string[:])    #string 변수의 처음부터 끝까지의 값을 가지고 옴 print(string) 이 코드와 같음음


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# string0 = 'cit academy'
# print(string0)

# split(문자열)
# 문자열을 문자열로 나누어 리스트트로 리턴
# 만약에 나눌 문자 없을 경우 해당 문자열 전체를 하나의 리스트로 생성
# print("split('a') :",string0.split('a'))

# count(문자열)
# 문자열에서 특정 문자열의 개수를 리턴 => 수를 알고 싶은 문자의 길이는 상관 없음
# 만약에 문자가 없을 경우 0을 리턴
# print("count('a') :",string0.count('a'))

# upper()     => 문자를 전부 대문자로
# lower()     => 문자를 전부 소문자로
# print('upper() :',string0.upper())
# print('lower():',string0.lower())

# replace(문자1, 문자2)
# 문자1을 문자2로 전부 변경
# 만약에 변경할 문자가 없는 경우 변경 안됨
# print("replace('a','A') :",string0.replace('a', 'A'))
# print(string0)
# string0 = string0.replace('a', 'A') # 이렇게 변수 재지정을 해야 변수에 대한 값이 변경됨됨
# print(string0)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# bookname = 'hello java'
# number = '20NB1A'
# print(bookname)
# print(number)
# print()

# print("Q1.bookname에서 'java'를 'python'으로 고치세요.")
# bookname = bookname.replace("java","python")
# print(bookname)
# print()

# print("Q2. bookname의 문자열 개수를 출력하시오")
# print(len(bookname))
# print()

# print("Q3.bookname에서 문자열을 모두 대문자로 바꾸시오.")
# bookname = bookname.upper()
# print(bookname)
# print()

# print("Q4. 두변수에 등장하는'A' 의 총개수를 출력하시오.")
# numA1 = bookname.count('A')
# numA2 = number.count('A')
# print(numA1+numA2)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# [이스케이츠 코드]
# 특별한 문자로 문자 출력시에 사용한다    => 띠옴표 기호('') 안에 있음
# \n     문자열 안에서 줄을 바꿀 때 사용
# \t     문자열 사이에 탭 간격을 줄 때 사용한다
# \\     문자 \를 그대로 표현할 때 사용한다
# \'     '를 출력
# \"     "를 출력

# print("Hello\nCIT")     # \n 사용
# print("Hello\tCIT")     # \t 사용
# print("Hello\\CIT")     # \\ 사용
# print("\'\"")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 문자열 합치기
# +기호를 이용하여 문자열을 합칠 수 있음
a = "hi"
b = "hello"
c = a + b
print(c)

# 문자와 숫자의 연산
# 문자의 숫자의 경우 곱하기(*) 만 가능
print("hello "*5)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#