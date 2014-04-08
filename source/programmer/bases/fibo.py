def fibo(n1,n):
	return n1+n
n2=0
n1=1
n0=0
for i in range(2,25):
	n2=n1+n0
	n0=n1
	n1=n2
	print n2		
	
