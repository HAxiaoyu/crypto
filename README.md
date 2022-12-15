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
第一步：
		选取n个随机整数d1 <d2 <d3 …<d1 <dn ,严格递增
		（di dj）=1,i≠j;
		N= d1 ×d2 ×…×dt M= dn-t+2 ×dn-t+3 ×…×dn N>M
		N>k>M
	第二步：
		任选t个子秘密对，计算
{█(x≡k_(i_1 )  mod d_(i_1 )  @x≡k_(i_2 )  mod d_(i_2 )@x≡k_(i_n )  mod d_(i_n ) )┤
		可以恢复秘密x≡k (mod N)
		任选t-1个子秘密对，不能恢复秘密。

参考数据1：[secret1.txt](https://github.com/HAxiaoyu/crypto/files/10233777/secret1.txt)
参考数据2：[secret2.txt](https://github.com/HAxiaoyu/crypto/files/10233778/secret2.txt)

#Elgamal公钥密码算法
密钥生成：
		(1)随机产生大素数p，得到模p的一个原根
		(2)产生随机整数a，计算g^a  (mod p)
		Alice的公钥是(p,g,ga)，私钥是a
	Bob加密过程：
		(1)随机产生整数k，2≤k≤p-2
		(2)计算c1≡g^k  (mod p), c2≡〖m*〖(g〗^a)〗^k  (mod p)
		(3)将密文发送给Alice
	Alice解密过程：
(1)计算v≡c_1^a  (mod p)
		(2)计算m≡c_2 v^(-1)  (mod p)
		验证m=c_2 v^(-1)  (mod p)

参考数据1：[secret1.txt](https://github.com/HAxiaoyu/crypto/files/10233784/secret1.txt)
参考数据2：[secret2.txt](https://github.com/HAxiaoyu/crypto/files/10233787/secret2.txt)

#SM2椭圆曲线公钥密码算法
参考数据在代码中
