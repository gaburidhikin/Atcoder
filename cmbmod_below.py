"""10**7>nだったら一度グラフを作ることで、それ以降の計算結果を
　　O(1)で返すことができる。グラフの計算にはO(n)"""


def cmb(n,r,mod):
    if r<0 or r>n:return 0
    r=min(r,n-r)
    return g1[n]*g2[r]*g2[n-r]%mod


mod=10**9+7
n=int(input())
g1=[1,1]
g2=[1,1]
inverse=[0,1]

for i in range(2,n+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1]%mod))

print(cmb(n,r,mod))