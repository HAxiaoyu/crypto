import random

def is_prime(m,k=5):#k为安全参数
    for _ in range(k):
        a=random.randrange(2,m-2)
        if gcd(a, m)!=1:
            return False
        if pow(a,m-1,m)!=1:
            return False
    return True

#求最大公约数
def gcd(a,b):
    if b==0: return a
    else: 
        return gcd(b, a%b)

# if __name__=='__main__':
#     #C将输入转为整数
#     m=int(input())
#     k=int(input())
#     p=float(pow(2,k))
#     if(is_prime(m,k)):
#         print("The probability that it is a prime number is {:.2%}".format(1-1/p))#输出m为素数的概率
#     else:
#         print("it's not a prime number")