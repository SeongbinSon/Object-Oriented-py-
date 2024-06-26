"""
try block : 오류가 발생하는지 테스트하는 블록
except block : 오류를 처리하는 블록
finally block : try와 except 블록이랑 상관없이 무조건 실행되는 블록
"""

#--------------------------------------------------------------------------#

try: #try문을 사용하여 오류가 발생하는지 테스트 할 수 있다.
   print(x) # type: ignore
except NameError: #except 문을 이용하여 NameError가 발생하면 그에 대한 처리를 할 수 있다.
   print("변수 정의 안됨") #실행결과를 출력할 수 있다.

#--------------------------------------------------------------------------#

def divide(a, b):
   try:
      c = a/b #try 문으로 c=a/b 문장을 테스트 한다
   except ZeroDivisionError: # 0으로 나누었을때 발생하는 ZeroDivisonError가 설정되고, 실행 결과의첫 번째줄에서와 같은 오류 메시지를 출력
      print("0 나누기 오류가 발생함!")
   else: #오류가 발생하지 않으면 그냥 C를 출력함
      print(c)

divide(30, 0)
divide(20, 10)

#--------------------------------------------------------------------------#

def get_value(list1, n):#정의된 함수 get_value(list1,n) 함수는 리스트 list1과 인덱스 n을 매개변수로 받아들여 인덱스 n에 해당되는 값을 반환하는 함수이다.
   try: #try문에 의해 result=list1[n] 문장을 테스트한다. 이 때 매개변수 n이 3의 값을 가지는데 인덱스 3은 리스트 list1, 즉 data의 범위를 벗어나고있음.
      result = list1[n]
   except IndexError: #리스트의 인덱스 오류
#(그 다음 문장이 수행되어 실행결과 첫 번째 줄에 오류 메시지를 출력함.
#그리고 result에 -1 값을 가지고 호출 함수로 돌아가
#실행 결과의 두번째 줄에서와 같이 -1을 출력함.)

      print("인덱스가 범위를 벗어남")
      result = -1
   finally: #  finally문은 위의 except문의 결과와 상관없이 무조건 수행된다. 따라서 변수 result를 호출함수에 반환한다.
      return result
   
data = [10,20,30]

print(get_value(data, 3)) #get_value(data, 3)으로 get_value(list1,n)에 정의돈 get_value()함수를 호출함

print(get_value(data, 1))
#get_value(data, 1)으로 get_value(list1,n)에 정의된 get_value()함수를 호출함.
#이 경우에는 get_value()함수에서 indexerror의 except문을 제외하고 모든 문장이 제대로 수행되어 실행 결과의 마지막 줄에 인덱스 1에 해당되는 20을 출력하게 된다.

#--------------------------------------------------------------------------#

"""
Class는 객체지향 프로그래밍의 핵심 요소 중 하나이다. 클래스를 이용하면 복잡한 프로그램을 좀 더 쉽고 체계적으로 작성하고 관리 할 수 있다.

클래스는 다음 그림에서와 같이 속성과 메소드로 구성된다.
"""
class Person:
   def hello(self):
      print("Hello.")

person1 = Person()
person1.hello()

#--------------------------------------------------------------------------#

class Person:
   name = "김정연"
   def hello(self):
      print(Person.name + "님 안녕하세요.")

person1 = Person()
person1.hello()

Person.name = "황서영"
person1.hello()

#--------------------------------------------------------------------------#

"""
클래스 : 속성과 메소드로 구성되는 객체 생성에 사용되는 틀
객체 : 클래스로부터 생성되어 해당 클래스의 속성과 메소드를 가진다.
속성 : 클래스와 객체 내부에서사용되는 변수를 의미한다.
메소드 : 클래스와 객쳋 내부에서 사용된느 함수를 의미한다.
"""

#--------------------------------------------------------------------------#

class Cat:
   kor_name = "로키"
   eng_name = "Rocky"
   age = 2

   def sound(self):
      print("야옹")

   def speed(self):
      print("엄청빠르다!")

mycat = Cat()

print("한글 이름 :", mycat.kor_name)
print("영어 이름 :", mycat.eng_name)
print("나이 :", mycat.age)
mycat.sound()
mycat.speed()

#--------------------------------------------------------------------------#

class Members:
   def set_info(self, name):
      self.name = name

   def show_info(self):
      print("이름:", self.name)

member1 = Members()
member1.set_info("홍지수")
member1.show_info()

member2 = Members()
member2.set_info("안지영")
member2.show_info()

#--------------------------------------------------------------------------#

class Members:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def show_info(self):
      print("이름:", self.name)
      print("나이:", self.age)

member1 = Members("황선영", 18)
member1.show_info()

member2 = Members("최종화", 32)
member2.show_info()

#--------------------------------------------------------------------------#

import math

class Circle:
   def __init__(self, r):
      self.r = r

   def get_area(self):
      result = math.pi * self.r * self.r
      return result
   
radius = float(input("반지름을 입력하세요 :"))

circle1 = Circle(radius)

print('반지름: %d ' % radius)
print('원의 면적: %.2f' % circle1.get_area())

#--------------------------------------------------------------------------#

class Scores:
   def __init__(self, name, kor, eng, math):
      self.name = name
      self.kor = kor
      self.eng = eng
      self.math = math

   def get_avg(self):
      sm = self.kor + self.eng + self.math
      avg = sm/3.0
      return avg
   
s1 = Scores("김성윤", 85, 90, 83)

print("이름 : %s" % s1.name)
print("국어 : %d, 영어 : %d, 수학 : %d" % (s1.kor, s1.eng, s1.math))
print("평균 : %.1f" % s1.get_avg())

#--------------------------------------------------------------------------#

class Calculator:
   def __init__(self, num1, num2):
      self.num1 = num1
      self.num2 = num2

   def add(self):
      result = self.num1 + self.num2
      print('%d + %d = %d' % (self.num1, self.num2, result))
   def sub(self):
      result = self.num1 - self.num2
      print('%d - %d = %d' % (self.num1, self.num2, result))
   def mul(self):
      result = self.num1 * self.num2
      print('%d x %d = %d' % (self.num1, self.num2, result))
   def div(self):
      result = self.num1 / self.num2
      print('%d / %d = %.2f' % (self.num1, self.num2, result))


a = int(input('첫번째 수를 입력하세요:'))
b = int(input('두번째 수를 입력하세요:'))

cal1 = Calculator(a, b)
cal1.add()
cal1.sub()
cal1.mul()
cal1.div()

#--------------------------------------------------------------------------#

class Student:
   pet = []
   def push_pet(self, x):
      self.pet.append(x)

john = Student()
john.push_pet("고양이")
print(john.pet)

sally = Student()
sally.push_pet("이구아나")
print(sally.pet)

#--------------------------------------------------------------------------#

class Members:
   total = 0

   def __init__(self, name, phone):
      self.name = name
      self.phone = phone
      Members.total = Members.total + 1

   def show_info(self):
      print("이름 : %s, 전화번호 : %s" % (self.name, self.phone))

m1 = Members("홍성지", "010-3359-3763")
m2 = Members("강동욱", "010-1019-4767")
m3 = Members("신진서", "010-9018-0298")

m1.show_info()
m2.show_info()
m3.show_info()

print("총 회원 수 :", Members.total)

#--------------------------------------------------------------------------#

class Person:
   def __init__(self, name):
      self.name = name

   def show_name(self):
      print(self.name)

class Student(Person):
   pass

x = Student("홍길동")
x.show_name()

#--------------------------------------------------------------------------#

class Person:
   def __init__(self, name):
      self.name = name
   def show_name(self):
      print(self.name)
   def show_age(self):
      print(self.age)

class Student(Person):
   def __init__(self, name, age):
      super().__init__(name)
      self.age = age

x = Student("홍길동", 20)
x.show_name()
x.show_age()

#--------------------------------------------------------------------------#

class Person:
   def __init__(self, name):
      self.name = name
   def show_name(self):
      print(self.name)

class Student(Person):
   def show_name(self):
      print("환영합니다!")
      print(self.name + "님 반갑습니다.")

x = Student("홍길동")
x.show_name()

#--------------------------------------------------------------------------#

class Employee:
   count = 0
   def __init__(self, name, position):
      self.name = name
      self.position = position
      Employee.count = Employee.count + 1
   def show_info(self):
      print("이름 : %s, 직위 : %s" % (self.name, self.position))

e1 = Employee("최진영", "대리")
e1.show_info()

e2 = Employee("김수정", "과장")
e2.show_info()

e3 = Employee("정선주", "부장")
e3.show_info()

print("총 직원 :", Employee.count)

#--------------------------------------------------------------------------#

class Rectangle():
   def __init__(self, width, height):
      self.width = width
      self.height = height
   def length(self):
      print("사각형 둘레:", self.width*2 + self.height*2)
   def area(self):
      print("직사각형 면적 :", self.width * self.height)

class Square(Rectangle):
   def __init__(self, a):
      super().__init__(a, a)
   def area(self):
      print("정사각형 면적 :", pow(self.width, 2))

s = Square(10)
s.length()
s.area()

#--------------------------------------------------------------------------#

class Calculator:
   a = 10
   b = 20

   def add(self):
      return self.a + self.b

c1 = Calculator()
print(c1.add())

# = 30 
#--------------------------------------------------------------------------#

class Calculator:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def add(self):
      return self.a + self.b
   
c1 = Calculator(10, 20)
print(c1.add())

# = 1. __init__
# = 2. c1.add()
#--------------------------------------------------------------------------#

class Triangle:
   def __init__(self, width, height):
      self.width = width
      self.height = height
   def area(self):
      print("삼각형 면적", self.width * self.height / 2)

#--------------------------------------------------------------------------#

class Father:
   def __init__(self, father_name):
      self.father_name = father_name
   def print_father(self):
      print("부모 : "+ self.father_name)

class Child(Father):
   def __init__(self, name1, name2):
      super().__init__(name1)
      self.child_name = name2
   def print_child(self):
      print("아이 : " + self.child_name)

father1 = Father("흥부모")
father1.print_father()
child1 = Child("최부모", "최아이")
child1.print_father()
child1.print_child()

#--------------------------------------------------------------------------#

class Buffer:
   def __init__(self):
      self.buffer = []
   def push_data(self, x):
      self.buffer.append(x)
   def get_data(self, index):
      return self.buffer[index]
   
buffer1 = Buffer()
buffer1.push_data(5)
buffer1.push_data(8)
buffer1.push_data(12)
print(buffer1.push_data)

print(buffer1.get_data(0))
print(buffer1.get_data(2))

#--------------------------------------------------------------------------#
