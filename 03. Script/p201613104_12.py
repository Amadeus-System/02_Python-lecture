# 12주차 파이썬 프로그래밍 과제
# p201613104_12


'''
# 1. 다음 문제를 보고 해결하라.
# 1.1) x를 2배로 만드는 익명함수를 만들고 실행하시오.

# lambda로 입력값의 2배 반환하는 익명함수 정의
x1 = lambda x : 2*x

# 출력 확인
print(x1(2))
print(x1(4))
'''


'''
# 1.2) 일반 함수를 이용하여 x를 2배로 만드는 함수를 만들고 실행하시오.

# def를 이용하여 일반적인 함수 정의
def x2(x):
    return 2*x  # 입력값의 2배 반환

# 출력 확인
print(x2(4))
print(x2(2))
'''



'''
# 1.3) 삼각형의 면적을 구하는 익명 함수를 작성하시오.
# 삼각형의 넓이 = 밑변a * 높이 b / 2

# 밑변a, 높이b를 입력받고 삼각형의 넓이 출력하는 익명함수 정의
tri = lambda a, b: a * b / 2  # 밑변 a, 높이 b 곱하고 2로 나눈 것
print(tri(13, 15))
print(tri(8, 10))
'''




'''
# 2. price 리스트에 상품 가격 5개의 정보가 다음과 같이 저장되어 있다.
# 모든 상품의 가격을 20% 세일한 값으로 출력하시오
# (람다 함수를 이용하여 작성한다.)

price = [1000, 2000, 3500, 4000]

for i in range(len(price)):  # price리스트 인덱스 i=0,1,2,3 에 대헤

    # 입력값의 20퍼센트 세일한 값 반환하는 람다함수 정의
    sale = lambda x: 0.8 * x

    if i == len(price) - 1:    # 마지막 리스트 요소에 대해서는
        print(sale(price[i]))  # 출력 마지막에 ,(컴마) 붙이지 않는다.
    else:  # 나머지 요소들에 대해서는
        print(sale(price[i]), end=', ')  # 줄바꿈 안하고 컴마, 공백 붙여 출력
'''




'''
# 3. 이전 실습에서 체중과 키로부터 비만도를 구하는 BMI 판정 프로그램을 만들었습니다.
# BMI는 체중(Kg)을 신장(m)의 제곱으로 나눈 값임.
# 사용자로부터 신장과 체중을 입력받아서 BMI값에 따라서
# 다음과 같은 메시지를 출력하는 프로그램을 작성하여 보자.


# 예외 처리를 이용하여 사용자가 0이라 입력하면 ZeroDivisionError 발생하며,
# 아무것도 입력하지 않으면 ValueError가 발생해 프로그램 끝나도록 코딩한다.


# 3.1)
# 사용자가 잘못 입력했을 때, 다시 입력하라는 메시지를 표시하도록 예외처리를 추가하세요.
# (try except만 사용하여 2가지 오류 모두 똑같은 결과값 출력, 소수점 3자리까지)

while True: # 무한루프 시작
    try: # 실행할 코드

        # 표준입력으로 무게(kg)와 키(m) 입력받는다.
        weight = int(input("무게(kg) 입력 : "))
        height = float(input("키(m) 입력 : "))

        # BMI 정의
        BMI = weight / (height*height)
        print("당신의 BMI : %.3f" % BMI)

        # BMI 범위에 따른 비만도 판정결과 출력
        if 20 < BMI < 24.9:
            print("정상입니다.")
            break  # 무한루프 벗어난다
        elif 25 < BMI < 29.9:
            print("과체중입니다.")
            break  # 무한루프 벗어난다
        elif BMI >= 30:
            print("비만입니다.")
            break  # 무한루프 벗어난다

    except ZeroDivisionError:   # 0으로 나눠 에러발생할 경우
        print("입력한 값에 문제가 있습니다. 다시 입력해 주세요. ")
        continue # 다시 루프 시작

    except ValueError:  # 사용자가 잘못 입력했을 경우
        print("입력한 값에 문제가 있습니다. 다시 입력해 주세요. ")
        continue # 다시 루프 시작
'''






'''
# 2) 이번에는 각각의 오류에 따라 다른 메시지가 나오도록 출력하시오.
# ZeroDivisionError : 숫자를 0으로 나눌 수 없습니다.
# ValueError : 값을 입력하지 않았습니다.

while True: # 무한루프 시작
    try:
        # 표준입력으로 무게(Kg)과 키(m) 입력받는다.
        weight = int(input("무게(kg) 입력 : "))
        height = float(input("키(m) 입력 : "))

        # BMI 계산한다.
        BMI = weight / (height*height)
        print("당신의 BMI : %.3f" % BMI) # 소수점 3번째 자리까지만 출력

        # BMI 값에 따른 비만도 판정 결과 출력
        if 20 < BMI < 24.9:
            print("정상입니다.")
            break  # 무한루프 벗어난다
        elif 25 < BMI < 29.9:
            print("과체중입니다.")
            break  # 무한루프 벗어난다
        elif BMI >= 30:
            print("비만입니다.")
            break  # 무한루프 벗어난다

    except ZeroDivisionError as e:  # 0으로 나눠 에러 발생할 경우
        print("숫자를 0으로 나눌 수 없습니다.", e) # 오류 메시지 함께 출력
        continue  # 다시 루프 시작

    except ValueError as e:  # 값을 잘못 입력하여 에러 발생할 경우
        print("값을 입력하지 않았습니다.", e) # 오류 메시지 함께 출력
        continue  # 다시 루프 시작
'''




'''
# 4번. 14장 모듈과 패키지 28page를 직접 작성하고 실행하라.
# 전제조건 : pip를 이용하여 requests, Beautifulsoup 패키지 깔기 p20 ~ 28 참조)

# 필요한 모듈 import
from urllib import request
from bs4 import BeautifulSoup

# url 주소 받아열기
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stndId=108")

# 파싱하기
soup = BeautifulSoup(target, 'html.parser')

# 필요한 정보를 출력한다.
for location in soup.select("location"):
    print("도시 :", location.select_one("city").string, end=' ')
    print("날씨 :", location.select_one("wf").string, end=' ')
    print("최저기온 :", location.select_one("tmn").string, end=' ')
    print("최고기온 :", location.select_one("tmx").string, end=' ')
    print()

'''









