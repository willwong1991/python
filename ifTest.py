# -*- coding: utf-8 -*-
weight = 1.75
height = 80

weight = float(input("please enter your weight :"))
height = float(input("please enter your height :"))
bmi = weight/(height * height)

print(bmi)
if bmi <= 18.5 :
    print("太轻了")
elif bmi<= 25 :
    print("正常")
elif bmi <= 28 :
    print("过重")
elif bmi <= 32 :
    print("肥胖")
else :
    print("严重肥胖")

print("done")