import fermat
import random
import CRT

#生成随机大素数
def get_prime():
    while True:
        p = random.randrange(10**150, 10**151)
        if fermat.is_prime(p):
            return p

#得到p的原根
def yg(p):
    k = (p-1)//2
    for i in range(2, p-1):
        if pow(i, k, p) != 1:
            return i

#加密过程
def jiami(p, g, y, m):
    while True:
        k = random.randint(2, p-2)
        if fermat.gcd(k, p-1) == 1:
            break
    c1 = pow(g, k, p)
    c2 = (m*pow(y, k, p)) % p
    return c1, c2

#解密过程
def jiemi(c1, c2, a, p):
    v = pow(c1, a, p)
    tmp = CRT.exgcd(v, p)
    m1 = c2*tmp % p
    return m1


file = open("D:/tmp/secret0.txt", 'r')
m = int(file.readline())
print(m, end='\n')

p = get_prime()
print(p, end='\n')

a = random.randint(2, p-2)
g = yg(p)
print(g, end='\n')

y = pow(g, a, p)
print(y, end='\n')

c1, c2 = jiami(p, g, y, m)
m1 = jiemi(c1, c2, a, p)
print(m1, end='\n')

print(m == m1)
