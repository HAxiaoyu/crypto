x,y=1,0

# 求最大公约数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# 判断列表中的mi是否两两互素
def is_prime(list):
    for i in range(0,len(list)):
        for j in range(i+1, len(list)):
            if gcd(list[i], list[j]) != 1:
                print("不能直接利用中国剩余定理")
                exit()

# 计算mi乘积
def get_multi(list):
    m = 1
    for i in list:
        m *= i
    return m

# 生成Mj=m/mj的列表
def get_div(m, list):
    div = []
    for i in list:
        div.append(m//i)
    return div

# 计算Mj的逆再模m
def exgcd(M, m):
    global x,y
    if m == 0:
        x, y = 1, 0
        return x
    exgcd(m, M % m)
    x, y = y, x
    y -= (M//m)*x
    return x

# 计算xj=(M*exgcd(M,m)*a)%m
def get_x(c, b, a, m):
    ans = (c*b*a) % m
    return ans

# 中国剩余定理
def CRT(list_a, list_m):

    is_prime(list_m)

    m = get_multi(list_m)
    list_M = get_div(m, list_m)

    list_M1 = []
    for i in range(len(list_M)):
        
        list_M1.append((exgcd(list_M[i], list_m[i])%m+m)%m)
    
    list_x = []
    for i in range(len(list_M)):
        list_x.append(get_x(list_M[i], list_M1[i], list_a[i], m))

    ans = 0
    for x in list_x:
        ans += x
        
    print(ans % m)
    return ans%m
# if __name__ == '__main__':
    
#     list_a=[]
#     list_m=[]
# #将文件中的前三行ai写入list_a,后三行写入list_m
#     file=open("D:/tmp/4.txt",'r')#通过此处修改1/2/3/4.txt传入不同文件
#     for i in range(3):  list_a.append(int(file.readline()))
#     for i in range(3):  list_m.append(int(file.readline()))
    
#     CRT(list_a,list_m)
