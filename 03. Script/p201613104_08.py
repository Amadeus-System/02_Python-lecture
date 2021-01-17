
'''
# 1번. 먼저 key가 정수이고, value가 정수의 제곱인 딕셔너리를 만들어보자.
# 편의상 0 ~ 4 까지만 생성한다.
# 1.1) 반복문을 이용한 방법, 딕셔너리 표현식을 이용한 방법 2가지로 작성하여라.

# 반복문 이용한 방법
a = {}  # 빈 딕셔너리
for i in range(5):
    a[i] = i ** 2
print(a)


# 딕셔너리 표현식 이용한 방법
b = {i : i**2 for i in range(0, 5)}
print(b)
'''



'''
# 1.2) 이 결과에서 값이 10 이하인 딕셔너리만 생성하라.
# 반복문을 이용한 방법, 딕셔너리 표현식 이용한 방법 2가지로 작성하라.

# 반복문 이용한 방법
a = {}
for i in range(5):
    if i**2 <= 10:  # 값이 10 이하일 때만
        a[i] = i**2 # 그 값을 할당

print(a)


# 딕셔너리 표현식 이용한 방법
b = {i : i**2 for i in range(0, 5) if i**2 <= 10}
print(b)
'''


'''
# 2번. 2의 거듭제곱 리스트 생성하기

# 표준입력으로 정수 2개가 입력된다.
# 첫번째 입력범위 : 1 ~ 20
# 두번째 입력범위 : 10 ~ 30
# 첫번째 값은 두번째 값보다 항상 작다.
# 첫번째 정수부터 두번째 정수까지를 지수로 하는 2의 거듭제곱 리스트를 출력하는 프로그램을 생성하고,
# 리스트의 두번째 요소, 뒤에서 두번째 요소는 삭제한 후 출력하라.

a, b = map(int, input('두 수를 입력 : ').split())

power_2 = []  # 빈 리스트 생성

for i in range(a, b + 1):
    power_2.append(2**i)

del power_2[1]  # 앞에서 두번째 요소 삭제
del power_2[-2] # 뒤에서 두번째 요소 삭제

print(power_2)
'''



'''
# 3번.
# 간단한 테이블 형태의 데이터를 2차원 리스트로 표현하자.
# 2개의 주사위 굴리면 다음과 같이 36가지의 결과가 나온다.

# 1) 첫번째 6 by 6, 0으로 초기화된 리스트 생성(리스트 표현식 사용)

a = [[0 for i in range(6)] for j in range(6)]
print(a)


# 2) 이를 이용하여 각각의 주사위가 나왔을 때의 합으로 표현하자.

a = [[i + j for i in range(1, 7)] for j in range(1, 7)]
print(a)
'''




'''
# 4번. 다음과 같은 출력 결과를 가지는 중첩 딕셔너리를 생성 하시오.

menu1 = {'hot_coffee': {'americano':3000, 'caffe_latte':3500, 'vanilla_latte':4000},
         'snacks': {'새우깡':700, '홈런볼':1000, '꼬깔콘':1500}}

print(menu1)


# 2) 편의점 메뉴가 늘어났다.

menu1['ice_coffee'] = {'americano':3000, 'caffe_latte':3500, 'vanilla_latte':4000}

print(menu1)



# ice_coffee 의 가격이 현재 hot_coffee의 가격과 동일하다.
# 가격을 올리기 전에 복사를 통해서 이전메뉴를 보존하고, 새로 복사한 메뉴에 ice_coffee 항목의 가격을 반복문을 사용하여
# 500원씩 올리고 결과를 출력하세요(이전 메뉴 menu1, 새로운 메뉴 menu2)

import copy
menu2 = copy.deepcopy(menu1)  # copy 모듈의 deepcopy 함수 이용하여 깊은 복사

print(menu2)
for key in menu2['ice_coffee'].keys():
    menu2['ice_coffee'][key] += 500

print(menu1)
print(menu2)
'''




