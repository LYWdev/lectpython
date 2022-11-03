# percet AND Gate
from itertools import tee
from operator import xor
import re
from matplotlib import pyplot as plt
import numpy as np

theta = 0


def AND(x1, x2):
    w1, w2, b = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2 - b
    if tmp <= theta:
        return 0ㅉ
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2  # 데이터 편향방지용
    tmp = np.sum(x*w)+b
    if tmp <= theta:
        return 0
    else:
        return 1


def NAND(x1, x2):
    w1, w2, b = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2 - b
    if tmp <= theta:
        return 1
    else:
        return 0


# 넘파이 응용한 배열 처리
x = np.array([-1.0, 1.0, 2.0])
y = x > 0
print(y)


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


print(xor(0, 0))
print(xor(0, 1))
print(xor(1, 0))
print(xor(1, 1))


print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))

print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))


# 행렬곱
A = np.array([[1, 2], [3, 4]])
print(A.shape)
B = np.array([[5, 6], [7, 8]])
print(B.shape)  # 행렬의 모양 표현

n = np.dot(A, B)  # 행렬 곱함수
print(n)

# 신경망 구현하기
X = np.array([-5.0, 5.0, 0.1])
x = np.arange(-5.0, 5.0, 0.1)


def sigmoid(x):
    return 1/(1+np.exp(-x))


def relu(x):
    return np.maximum(0, x)


y = sigmoid(x)

W1 = np.array([1.0, 0.3, 0.5], [0.2, 0.4, 0.6])
# B1 = np.array([1.0, 0.2, 0.3])
plt.ylim(-0.1, 1.1)
plt.plot(x, y)
plt.show()
print(sigmoid(X))
