
# short python intro
from cProfile import label
from ipaddress import collapse_addresses
from re import I, X
from tkinter import Y
from unicodedata import name
import numpy as np
import matplotlib.pylab as plt
from matplotlib.image import imread

# I/O function


# class 'int'
# class 'float'
# class 'str'
# class 'bool'
# print('hello')
# name = input("name : ")
# print(name)

# 반지름이 R인 피자를 N 명과 공평히 나눔.
# 나는 얼마만큼 먹는가?
# r = float(input("피자의 반지름은 얼마인가"))
# s = 3.14*r**2
# n = int(input("넓이가 %.2f이고 우린 몇명인가?" % s))
# print("그럼 우리는 이낭 %g만큼 먹을 수 있다." % (s/n))
# 리스트
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a)
# n = len(a)
# print(n)
# a[2] = 0
# x = input()
# a.append(x)
# print(a)
# print(a[2:4])
# print(a[1:])
# print(a[:3])
# print(a[:-2])

# # tuple
# b = (1, 2, 3, 4, 5, 6)
# print(b)
# print(b[1:4])
# # 원소 접근하여 수정 안됨.
# b[0] = 1

# # 딕셔너리
# par = {'w1': 46, 'b1': 1, 'w2': 78, 'b2': 0}
# print(par)
# print(par['w1'])
# par['w3'] = 99
# print(par)
# par['w2'] = 13
# print(par)

# #조건문 !괄호가 없다.
# print('start')
# print('')
# color = input("횡단보도가 나왔다. 무슨색인가? : ")
# if('초') in color:
#     print("횡단보도를 잘 건넘")
# else:
#     print("기다림")

# # while 반복문
# num = int(input("확진자 수 :"))
# while num > 200:
#     print("거리두기 3주 연장")
#     print("--3주후--")
#     num = int(input("확진자 수:"))
# print("거리두기 끝")

# # for반복문
# print("구구단을 외자:")
# n = int(input("몇 단:"))
# for i in range(1, 10):
#     print("%d * %d = %d" % (n, i, n*i))

# # 계단 출력10
# N = int(input("계단 몇개?:"))
# for i in range(N):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# # 함수
# def f(x):
#     y=2*x+1
#     return y
# print("f(10)=", f(10))
# print("f(20)=", f(20))
# print("f(30)=", f(30))

# # 클래스
# class person:
#     name = None
#     age = 0

#     def info(self, pName, pAge):
#         self.name = pName
#         self.age = pAge

#     def intro(self):
#         print("Hello")
#         print("My Name : ", self.name)
#         print("Age", self.age)


# name = input()
# age = int(input())
# p1 = person()
# p1.info(name, age)
# p1.intro()

# # numpy
# x = np.array([1.0, 2.0, 3.0])
# print(x)
# # type를 통해 numpy배열 확인
# print(type(x))

# # 넘파이 산술 연산
# x = np.array([1.0, 2.0, 3.0])
# y = np.array([2.0, 4.0, 6.0])

# # 넘파이의 배열의 행,열의 개수가 같다. 다름 오류 발생한다.
# print("1", x+y)
# print("2", x-y)
# print("3", x*y)
# print("4", x/y)

# # 넘파이 브로드 캐스트 : 스칼라 행렬에 일정히 곱한다.
# print("5", x/2.0)

# # 넘파이 브로드 캐스트 : 다른 차원의 배열도 연산가능
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[10, 20]])
# print(A*B)

# # 원소 접근
# x = np.array([[51, 55], [14, 19], [0, 4]])
# print(x)
# print(x[0])
# print(x[0][1])
# print()
# for row in x:
#     print(row)
# x = x.flatten
# print(x)

# # # matplotlib
# x = np.arange(0, 6, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)

# # plt.plot(x, y)
# plt.show()
# plt.plot(x, y1, label='sin')  # label 정하기
# plt.plot(x, y2, label="cos")
# plt.xlabel("x")
# plt.xlabel("y")
# plt.title('sin & cos')  # Title
# plt.legend()
# plt.show()

# # Image read
# img = imread('cat.jpg')
# plt.imshow(img)
# plt.show()
