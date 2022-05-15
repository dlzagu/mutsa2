name = input("이름을 입력하세요:")
score = int(input("점수를 입력하세요 :"))

if score >= 90 :
    print(name, "의 학점 : A" )
elif score >= 80 :
    print(name, "의 학점 : B" )
elif score >= 70 :
    print(name, "의 학점 : C" )
elif score >= 60 :
    print(name, "의 학점 : D" )
else :
    print(name, "의 학점 : F" )