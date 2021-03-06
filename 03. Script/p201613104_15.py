# -*- coding: utf-8 -*-
"""p201613104_15

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RlVrBr4LLR1VZQng_9b1NR8v7EmTNQ8f
"""



# 1. 16장 24page의 클래스 메서드 사용하기 예제를 실행해보자.

# 클래스 선언
class Calc:
    
    history = []  # 클래스 속성

    @classmethod  # 클래스메소드 선언
    def history_fun(cls):  # 클래스메소드이므로 cls 인자 넣음
        for item in Calc.history:
            print(item)  # 클래스 속성에 넣은 값 출력하기
 
    # 속성 정의
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # 덧셈 연산 메서드
    def sum(self):
        result = self.num1 + self.num2
        Calc.history.append("add : " + str(result))  # 클래스 속성에 넣음
        return self.num1 + self.num2

    # 뺄셈 연산 메서드
    def sub(self):
        result = self.num1 - self.num2
        Calc.history.append("sub : " + str(result))  # 클래스 속성에 넣음
        return self.num1 - self.num2

# 출력 확인!
C2 = Calc(20, 10)  # 인스턴스 생성
print(C2.sum())
print(C2.sub())
Calc.history_fun()





# 문제 2.
# 편의점에서 알바생과 점장이 일을 한다.
# 알바생 : 월급만 있음
# 점장 : 월급 외에 보너스가 있다


# 알바생 클래스 선언
class Employee:
    
    # 이름과 월급을 속성으로 가진다.
    def __init__(self, name, salary):
        self.name = name      # 이름(문자열)
        self.salary = salary  # 월급(정수형)

    # 월급 반환하는 메소드
    def getSalary(self):
        return self.salary
    

# 점장 클래스 선언 : 상속으로 정의
class Manager(Employee):
     
    # 이름, 월급, 보너스를 속성으로 가짐.
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)  # 기반클래스의 속성값 정의를 가져와서 파생클래스에서 써서 중복을 줄인다.
        #self.name = name
        #self.salary = salary
        self.bonus = bonus   # 기반클래스에서만 쓰는 추가적인 속성 정의
    
    # 메소드 재정의 : 메소드 오버라이딩
    def getSalary(self):
        return self.salary + self.bonus  # 보너스를 월급에 더해서 리턴


# 출력 확인!
lee = Employee('이현식', 2000000)
hong = Manager('홍길동', 2000000, 500000)
print("이름 :", lee.name, "월급 :", lee.salary)
print("이름 :", hong.name, "월급 :", hong.salary, "보너스 :", hong.bonus)




# 문제 3번.

# 3.1) 은행계좌를 나타내는 클래스를 정의한다.
# 클래스 이름은 Bank_Account
# 지난시간에는 현재잔액(balance)만을 변수로 가졌지만
# 이번에는 소유자의 이름, 통장번호를 추가한다.


# 은행계좌 클래스 선언
class Bank_Account:
    
    # 이름, 통장번호, 현재잔액을 속성값으로 가진다.
    def __init__(self, name, number, balance):
        self.name = name        # 소유자 이름, 문자열
        self.number = number    # 통장 번호
        self.balance = balance  # 잔액, 정수형

    # 출금 메소드
    def withdraw(self, x):
        if x <= self.balance:   # 출금하려는 금액이 잔액보다 작거나 같을 때만
            self.balance -= x   # 현재잔액에서 x만큼 출금한다.
            print(self.balance) # 남은 잔액 보여준다.

    # 입금 메소드
    def deposit(self, x):   # x만큼 입력받아 예금
        self.balance += x   # 입금 금액만큼을 현재잔액(balance)에 더해 저장
        print(self.balance) # 남은 잔액 보여준다


# 3.2) Bank_Account 클래스를 상속받아 Savings_Account 클래스를 작성한다.

# Savings_Account 클래스 선언
class Savings_Account(Bank_Account):

    # 이름, 통장번호, 현재잔액, 이자율의 속성을 가진다.
    # 이 중 이름, 통장번호, 현재잔액은 기반클래스와 겹치는 속성이므로 super()로 가져다 쓸 수 있음
    def __init__(self, name, number, balance, interest_rate ):
        super().__init__(name, number, balance)  # 기반클래스의 속성을 가져다 쓸 수 있음, 중복 줄이기
        self.interest_rate = interest_rate   # 이자율(실수형), 파생 클래스의 추가속성 정의
        #self.balance = balance
        #self.name = name
        #self.number = number

    # 호출 될때마다 예금에 이자를 더하는 메소드
    def add_interest(self):
        self.balance += (self.interest_rate * self.balance)


# 3.3) Bank_Account 클래스를 상속받아 Checking_Account 클래스를 작성한다.

# Checking_Account 클래스 선언
class Checking_Account(Bank_Account):

    # 이름, 통장번호, 현재잔액을 속성으로 가진다.
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)   # 기반클래스의 속성값 가져와서 쓴다
        #self.name = name
        #self.number = number
        #self.balance = balance
        self.withdraw_charge = 500   # 추가속성, 수수료(정수형) 정의
        

    # 찾을 금액에 수수료를 더해서 출금하는 메소드
    def withdraw(self, x): # 메소드 오버라이딩
        
        output = x + self.withdraw_charge
        if output <= self.balance :  # 출금금액 + 수수료가 현재잔액보다 작거나 같으면
            self.balance -= output   # 그만큼 잔액에서 뺀다.
            print("출금 :", output)  # 출금


# 출력 확인!
a1 = Savings_Account("이현식", 123456, 10000, 0.05)
a1.add_interest()  # 메소드 실행
print("저축예금 잔액 :", a1.balance)

a2 = Checking_Account("이현식", 654321, 200000)
a2.withdraw(100000)



