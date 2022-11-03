# m = 2
# a = 1
# for n in range(1, 10):
#     print("{} * {} = {}".format(m, n, m*n))

start = 1
end = 31

# days ={""}
# days = []
# days[0] = '월'
# days[1] = '월'
# days[2] = '화'
# days[3] = '수'
# days[4] = '목'
# for i in range(0, 5):
# days[i]
for day in range(start, end+1):
    print("5월 {}일은 {}요일입니다".format(day, days[(day, days[day+5] % 7)]))

list = {"name": "반근우", "job": "선생님"}
# range(len(list))
key = list.keys()
for i in list:
    print(list[i])
