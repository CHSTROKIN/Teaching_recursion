import time
import matplotlib.pyplot as plt
def func(n):
	if(n==0):
		return 0
	else:
		if(n==1):
			return 1
		else:
			return func(n-1)+func(n-2)
total=[0,1]
def func2(n):
	if(len(total)>n):
		return total[n]
	else:
		total.append(func2(n-1)+func2(n-2))
		return total[n]
def func3(n):
	a=1
	b=0
	sum=0
	for i in range(1,n):
		sum=a+b
		b=a
		a=sum
	return sum

if __name__ == '__main__':
	print("this program is used as main program:not initiate test sequence")
	'''
	test sequence will inculude the using of following functions:
		func(n):n is an integer
		func2(n):n is an integer
		func3(n):n is an integer
	'''	
	list=[]
	listv=[]
	list2=[]
	list3=[]
	for i in range(1,100):
		t1=time.time()
		print(func2(i))
		t2=time.time()
	#	print((t2-t1))
		list.append(t2-t1)
		listv.append(i)
		t3=time.time()
		print(func(i))
		t4=time.time()
	#	print(t4-t3)
		list2.append(t4-t3)
		t5=time.time()
		print(func3(i))
		t6=time.time()
		list3.append(t6-t5)
		print("__________________")
	print("this is end of the test")
	print(time.time())
	plt.plot(listv,list,listv,list2,listv,list3)
	plt.show()


