import CRT
import random

secret_list = []
di_list = []
ki_list = []
lenth=0

# 互素判断
def is_mutual(list, x):
    for i in list:
        if CRT.gcd(i, x) == 1:
            continue
        else:
            return 0
    return 1

# 生成不重复且互质的随机数
def randint_generater(min, max, count):
    global lenth
    t=lenth//3
    list = []
    list.append(random.randint(pow(10, t), pow(10, t+1)))
    while len(list) != count:
        unit = random.randint(min, max)
        if unit not in list:
            if is_mutual(list, unit) == 1:
                list.append(unit)
    return list

# 生成(di,ki)对并验证结果
def solution(k, n, t):
    temp = k
    global lenth
    while temp > 0:
        temp=temp//10
        lenth += 1
    di_list = randint_generater(pow(10, lenth//3), pow(10, lenth/3), 5)
    di_list.sort()
    for i in di_list:
        ki_list.append(k % i)
    # 生成子秘密
    secret_list = list(zip(di_list, ki_list))
    print(secret_list)
    list_a = []
    list_m = []
    tmp = []
    tmp = random.sample(range(0, n), t)
    # 随机选取秘密对
    for i in tmp:
        list_a.append(ki_list[i])
    for i in tmp:
        list_m.append(di_list[i])
    # 利用中国剩余定理还原秘密
    ans = CRT.CRT(list_a, list_m)
    print(ans == k)


file = open("D:/tmp/secret1.txt", 'r')
k = int(file.readline())
solution(k, 5, 3)
