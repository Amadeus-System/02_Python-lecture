

# 3주차 실습

'''
# 기본 연산자 연습
# IDLE에서 다음 수식을 직접 실행시켜보자.

print(31 + 26)

print(511 - 54)

print(5 * 15)

print(96 / 4)
'''



'''
# 다음 문장의 실행결과를 예측하여 보고 결과를 출력하라.


print(20 % 6)   # 나머지만 출력

print(21 / 5)    # 일반적인 나눗셈 - 실수형 출력

print(21 // 5)   # 몫만 정수로 출력
'''




'''
# 연산자

# 다음 수식을 직접 실행시켜보자.

print(2 ** 4)   # 2의 4승
print(4 ** 6)   # 4의 6승


# 다음 수식을 직접 실행시켜보자.

print(3.1 ** 4.2) # 거듭제곱 연산 실행
print(2.6 ** 5.4)
'''



'''
# 연산자 우선 순위

# 다음 수식을 직접 실행시켜보자.

print((2 + 4) * 5)     # 괄호 안을 먼저 계산 
print(4 * (26 - 9))
print((4 + 5) ** (9-6))

# 다음 수식을 직접 실행시켜보자.

print(4 * 6 - 5)    # 곱셉 먼저 연산하고 뺄셈  
print(9 + 54 / 6)   # 나눗셈 먼저 연산하고 덧셈 

# 다음 수식을 직접 실행시켜보자.

print( 2**4 + 5)     # 거듭제곱 먼저 하고 덧셈 
print( 6 * 5 ** 2)   # 거듭제곱 먼저하고 앞의 곱셈 
'''



'''
# 연산자들의 복합
# 다음 수식을 직접 실행시켜본 후 결과를 확인해보자.

print(5 * 4 + 6)         # 곱셈 먼저하고 덧셈
print(26 + 20 / 2)      # 나눗셈 먼저하고 덧셈 -> 실수형 출력
print( (511//31) ** (9 - 6) )   # 괄호 안을 각각 먼저 계산
'''




'''
# 실수가 포함된 수식 계산하기
# 다음 수식을 직접 실행시켜본 후 결과를 확인해보자.

print(8.2 * 4 + 2)   # 곱셈 먼저하고 덧셈

print(20 + 9 / 4.5)  # 나눗셈 먼저하고 덧셈 -> 실수형출력

print( (15.1/4) ** (6 - 4) ) # 괄호안을 각각 먼저 계산
'''




'''
# 다음 문장의 실행 결과를 예측해보고 실행하여 비교해보아라.

print(5 + 12 // 7 * 3) # 몫 연산 -> 곱셈 -> 덧셈 

print(15 / 2 + 21 % 4 - 2 ** 3) # 나눗셈, 나머지연산, 거듭제곱 각각 먼저하고 더하고 뺀다.
'''




'''
# 자료형 확인
# type 함수를 이용하여 다음에 해당하는 자료형을 확인해보자.

print(type(10))   # 정수형 int

print(type(10.0)) # 실수형 float
'''



'''
# string 형의 예

tom = 'Boy'
print(tom)

bob = 'I am a boy'
print(bob)
'''




'''
# string 형의 예

print('"He is a smart boy." my teacher said')

print("He`s a smart and diligent boy.")

# print('He`s a smart and diligent boy.`)   # 따옴표 잘못사용하면 syntax에러 발생 
'''



'''
# string 형의 예

start = '=========='
title = 'Python Program'
finish = '=========='

print(start + title + finish)
'''



'''
# 다음 문장의 실행결과를 예측해보고 실행하여 비교해보아라.

name = 'Gildong'
location = 'Seoul'

print('Hello, My name is '+ name +'. And I live in ' + location + '.')
'''



'''
# string 형의 예

start = '=' * 10
title = 'Python Program'
finish = '=' * 10

print(start + title + finish)
'''




'''
# 다음 문장의 실행 결과를 예측해보고 실행하여 비교해 보아라.

string1 = 'Hello,'
string2 = ' Python'
star = '*******'
star = '***'   # 변수에 할당된 값이 갱신된다.

print(star * 3 + string1 + string2 + star*3)   # 별 9개씩 앞뒤에 달린다.

'''



'''
# 입력 예제

name = input('이름을 입력하시오')

print(name)


name = input('What is your first name? ')

print(name)
'''



'''
# 입력 예제
# 다음 명령문을 활용하여 스케줄을 작성해보자.

applicant = input("Enter the applicant`s name: ") # Gildong 입력

interviewer = input("Enter the interviewer`s name: ") # Minwoo 입력

time = input("Enter the appointment time: ") # 14:00 입력

print(applicant)
print(interviewer)
print(time)
'''



'''
# 다음 소스 코드를 완성하여 정수 3개를 입력받고 합계가 출력되게 하라.

a = int(input('더할 수를 입력하세요:'))   # -10 입력
b = int(input('더할 수를 입력하세요:'))   # 20 입력
c = int(input('더할 수를 입력하세요:'))   # 30 입력

print(a + b + c)
'''



'''
# 출력 예제

print('True Love')

number1 = 26   # 각 변수에 수를 할당한다.
number2 = 31

sum = number1 + number2   # 두 수를 더해서 sum에 저장 
                                     # sum 을 변수명으로 함부로 써도 되는지..??
print(sum)
'''



'''
# 출력 예제
# 과목의 성적을 나타내주는 프로그램을 작성하고자 한다.

math = 54
english = 72
history = 96

print(math, english, history)
'''



'''
# 출력 예제
# 길이와 폭으로 넓이를 구해서 나타내주는 프로그램을 작성하고자 한다.

length = 9
width = 6

print('area = ', length * width)
'''



'''
# 다음 문장의 실행 결과를 예측해보고 실행하여 비교해보아라.

name = 'Gildong'   # name 변수에 문자열 할당

print('Hello, my name is', name)  # 할당된 문자열이 함께 출력된다
'''



'''
# 다음 소스코드를 완성하여 날짜와 시간이 출력되게 만들어라.

year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep='/', end=' ')  # 한줄로 출력하기 위해 end 설정 
print(hour, minute, second, sep=':')
'''





'''
# 강제 형변환

n = 7
n = float(n)   # 정수7을 실수로 형변환
print(type(n))
print(n)


n = input('enter the number : ')
n = int(n) # 입력받은 문자열을 정수로 형변환

print(type(n))
print(n)
'''



'''
# 자료형 변환
# 연필과 펜의 구입하는 개수에 따라 총 가격을 반환해주는 프로그램을 작성해보자

연필 = 1000
펜 = 2000

print('연필 =',str(연필) + '원')
print('  펜 =',str(펜) + '원')

      
num_pencil = int(input('\n연필은 몇 개를 구입하시겠습니까?: '))
num_pen = int(input('펜은 몇 개를 구입하시겠습니까?: '))

total_price = (연필 * num_pencil) + (펜 * num_pen)
total_price = str(total_price)

print('총 가격은 ' + total_price +'원 입니다') 
'''               
                   


'''
# Boolean형과 비교/논리 연산자

student_gender = 'female' # 수지는 여자이다.
grade = 2                      # 수지는 2학년이다

# 여성이고 1학년이어야 할인받으므로 and 를 사용한다.
print( (student_gender == 'female') and (grade == 1) )
'''



'''
# 어느회사의 입사조건은 토익점수가 800점 이상 이거나
# 교양 영어에서 A학점이 만족되어야 지원가능하다고 한다.

# 길동이의 토익점수와 교양영어 학점
toeic_score = 900
gradeOfEnglish = 'B'

# 토익점수 800점이상 이거나 A학점 조건 둘 중 하나만 성립해도
# 되므로 or을 사용한다

print( (toeic_score >= 800) or (gradeOfEnglish == 'B') )
'''




'''
# 평균 점수를 출력하는 프로그램 만드세요.

a , b, c, d = map(int, input('정수 4개를 입력하시오 : ').split())

print( (a + b + c + d) // 4)  # 정수 출력 


a , b, c, d = map(int, input('정수 4개를 입력하시오 : ').split())

print( (a + b + c + d) // 4)  # 정수 출력 
'''



'''

# 표준입력으로 년, 월, 일, 시, 분, 초가 입력되게 합니다.
# 입력된 날짜와 시간을 특정한 형식으로 출력하기

year, month, day, hour, minute, second = map(int, input('년, 월, 일, 시, 분, 초를 입력하시오 : ').split())

print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')
'''





























