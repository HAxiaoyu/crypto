from random import randint
import math
from gmssl import sm3
from gmssl import func
from CRT import exgcd
import binascii
# 函数传参是int的16进制类型 kdf传入的是字节串 输出时将int转16进制字符串

# 素数p：
p=0x8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3
# 系数a：
a=0x787968B4FA32C3FD2417842E73BBFEFF2F3C848B6831D7E0EC65228B3937E498
# 系数b：
b=0x63E4C6D3B23B0C849CF84241484BFE48F61D59A5B16BA06E6E12D1DA27C5249A
# 基点G=(xG,yG)，其阶记为n。
# 坐标xG：
xg=0x421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D
# 坐标yG：
yg=0x0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2
# 阶n：
n=0x8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7

# 待加密的消息M：
m=input("待加密的消息:")

def bitfill(x, size):#比特位填充
    if isinstance(x, int):
        if x >> (size << 3): # 指定的字节数不够则截取低位
            x &= (1 << (size << 3)) - 1
        return x.to_bytes(size, byteorder='big')
    elif isinstance(x, str):
        x = x.encode()
        if len(x) > size:
            x = x[:size] # 截取左侧字符
        return x
    elif isinstance(x, bytes):
        if len(x) > size:
            x = x[:size]
        return x
    return bytes(x)

def KDF(z, klen): # z传入的参数是字节类型
    ct=1
    K = ''
    for i in range(math.ceil(klen / 256)):
        K=K+(sm3.sm3_hash(func.bytes_to_list(z+ct.to_bytes(4,byteorder='big'))))
        ct+=1
    klen=klen//4
    return K[:klen]

def zuobiao(a,p,x1,y1,x2,y2):#椭圆曲线加法计算坐标
    if x1==x2 and y1==p-y2:
        return False

    if x1!=x2:
        lamda=((y2-y1)*exgcd(x2-x1, p))%p
    else:
        lamda=(((3*x1*x1+a)%p)*exgcd(2*y1, p))%p

    x3=(lamda*lamda-x1-x2)%p
    y3=(lamda*(x1-x3)-y1)%p
    return x3,y3

def beidian(a,p,x,y,k):#倍点计算
    k=bin(int(k,16))
    dx,dy=x,y
    for i in range(1,len(k)):
        dx,dy=zuobiao(a, p,dx, dy, dx, dy)
        if k[i]=='1':
            dx,dy=zuobiao(a, p,dx, dy, x, y)
    return dx,dy

def encrypt(a,p,n,m,db,xb,yb,xg,yg,k):#加密过程
    # 打印消息m:temp
    temp=format(int(m.encode().hex(),16),'x')
    print("消息m:",temp.upper())
    # t不为0
    while True:
        k=randint(1,n-1)
        k=bitfill(k,32).hex()
        while k==db:
            k=randint(1,n-1)
            k=bitfill(k,32).hex()
        print("随机数k:",k.upper())
        x2,y2=beidian(a,p,xb,yb,k)
        x2="{:064x}".format(int(hex(x2),16),'x').encode()
        y2="{:064x}".format(int(hex(y2),16),'x').encode()
        z=binascii.unhexlify(x2+y2)
        t=KDF(z,len(temp)*4)
        if bin(int(t,16))!=0:
            break
    #t
    print("计算t:",t.upper())
    #c1
    x1,y1=beidian(a,p,xg,yg,k)
    x1=format(int(hex(x1),16),'x').upper()
    y1=format(int(hex(y1),16),'x').upper()
    c1='04'+x1+y1
    #c2
    c2=int(temp,16)^int(t,16)
    tmp=format(int(hex(c2),16),'x')
    print("计算c2:",tmp.upper())
    #c3
    m_temp=bytes(temp,encoding='UTF-8')
    z_temp=binascii.unhexlify(x2+m_temp+y2)
    c3=sm3.sm3_hash(func.bytes_to_list(z_temp))
    print("计算c3:",c3.upper())
    #c
    c=(c1+tmp+c3).upper()
    print("密文c:",c)
    return c1,tmp,c3

def decrypt(c1,tmp,c3,db,a,b,p):#解密过程
    c1=c1[2:]
    x1=int(c1[:len(c1)//2],16)
    y1=int(c1[len(c1)//2:],16)
    if pow(y1,2,p)!=(pow(x1,3,p)+a*x1+b)%p:
        return False
    x2,y2=beidian(a,p,x1, y1, db)
    x2="{:064x}".format(int(hex(x2),16),'x').upper()
    y2="{:064x}".format(int(hex(y2),16),'x').upper()
    print("坐标x2:",x2)
    print("坐标y2:",y2)

    z=(x2+y2).encode()
    z_tmp=binascii.unhexlify(x2+y2)
    klen=len(tmp)*4
    t=KDF(z_tmp,klen)
    print("计算t:",t.upper())
    if bin(int(t,16))==0:
        return False
    # 解密
    m_d_temp=int(t,16)^int(tmp,16)
    m_d=format(int(hex(m_d_temp),16),'x')
    print("解密m:",m_d.upper())
    #u
    u_temp=bytes((x2+m_d+y2),encoding='UTF-8')
    u_tmp=binascii.unhexlify(u_temp)
    u=sm3.sm3_hash(func.bytes_to_list(u_tmp))
    print("验证:",u==c3)


db=randint(1,n-1)
db=bitfill(db,32).hex()
print("随机数db:",db.upper())

xb,yb=beidian(a,p,xg,yg,db)

k=randint(1,n-1)
k=bitfill(k,32).hex()

c1,tmp,c3=encrypt(a,p,n,m,db,xb,yb,xg,yg,k)

decrypt(c1,tmp,c3,db,a,b,p)