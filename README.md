# Cryptography Experiments

#fermat.py 费马素性检测算法
给定奇整数m≥3和安全参数k
	随机选取整数a,2≤a≤m-2
	计算g=(a, m)，如果g =1，转（3）；否则，跳出，m为合数
	计算r=a^(m-1) (mod m) 如果r=1,m可能是素数，转（1）；否则，跳出，m为合数。
  重复上述过程k次，如果每次得到m可能为素数，则m为素数的概率为1-1/2^k  

参考数据1：[1.txt](https://github.com/HAxiaoyu/crypto/files/10233756/1.txt)
参考数据2：[3.txt](https://github.com/HAxiaoyu/crypto/files/10233757/3.txt)

#CRT.py 根据中国剩余定理求解同余方程组
参考数据1：[1.txt](https://github.com/HAxiaoyu/crypto/files/10233763/1.txt)
参考数据2：[2.txt](https://github.com/HAxiaoyu/crypto/files/10233766/2.txt)
参考数据3：[3.txt](https://github.com/HAxiaoyu/crypto/files/10233767/3.txt)
参考数据4：[4.txt](https://github.com/HAxiaoyu/crypto/files/10233768/4.txt)

#(t,n)门限秘密共享方案

参考数据1：[secret1.txt](https://github.com/HAxiaoyu/crypto/files/10233777/secret1.txt)
参考数据2：[secret2.txt](https://github.com/HAxiaoyu/crypto/files/10233778/secret2.txt)

#Elgamal公钥密码算法

参考数据1：[secret1.txt](https://github.com/HAxiaoyu/crypto/files/10233784/secret1.txt)
参考数据2：[secret2.txt](https://github.com/HAxiaoyu/crypto/files/10233787/secret2.txt)

#SM2椭圆曲线公钥密码算法
参考数据在代码中
