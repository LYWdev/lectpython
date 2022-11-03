from turtle import forward
import load_mnist
from matplotlib import pyplot as plt
import numpy as np
import sys
import os
sys.path.append(os.pardir)  # 부모 디렉토리 파일 권한 할당
# x = np.array([1.0, 0.5])
# W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
# B1 = np.array([0.1, 0.2, 0.3])

# A1 = np.dot(x, W1)+B1


# def sigmoid(x):
#     return 1/(1+np.exp(-x))


# Z1 = sigmoid(A1)
# print(A1)
# print(Z1)

# a = np.array([0.3, 2.9, 4.0])
# exp_a = np.exp(a)  # 지수함수
# sum_exp_a = np.sum(exp_a)  # 지수 함수의 합

# print(exp_a/sum_exp_a)
class MulLyaer:
    def __init__(self):  # 인스턴스 변수 x,y초기화
        self.x = None
        self.y = None

    def forward(self, x, y):  # x와 y를 인수로 두고 두 곱하고 반환
        self.y = y
        self.x = x
        out = x*y
        return out

    def backward(self, dout):
        dx = dout*self.y  # SWAP(x,y)
        dy = dout*self.x

        return dx, dy
