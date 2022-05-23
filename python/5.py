# 1번

  def plus(num1, num2):
     return num1 + num2
 def minus(num1, num2):
     return num1 - num2
 def multi(num1, num2):
     return num1 * num2
 def divide(num1, num2):
     return num1 / num2
     
 while True:
     num1, num2 = map(int, input("연산을 진행할 두 숫자를 입력하세요: ").split())
     q = input("어떠한 연산을 수행할까요? ")

     if q == '+':
         print("{} {} {} = {}\n".format(num1, q, num2, plus(num1, num2)))
    
      elif q == '-':
         print("{} {} {} = {}\n".format(num1, q, num2, minus(num1, num2)))
    
      elif q == '*':
         print("{} {} {} = {}\n".format(num1, q, num2, multi(num1, num2)))
    
      elif q == '/':
         print("{} {} {} = {}\n".format(num1, q, num2, divide(num1, num2)))
    
     else:
        print("해당 연산은 지원하지 않습니다.\n")

    
