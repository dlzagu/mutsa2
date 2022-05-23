import random
import time

def lotto():
    num = random.sample(range(1,46),6)
    num.sort()
    for i in range(1,6):
        print(f'{i}..')
        time.sleep(1)
    print("로또 번호는!!")
    print(f'{num}입니다.')

a = input(("로또번호 추출을 시작합니까?(y/n) : "))

if a == 'y':
    print("번호 추출중..")
    lotto()
elif a == 'n':
    print("로또 추출을 종료합니다.")