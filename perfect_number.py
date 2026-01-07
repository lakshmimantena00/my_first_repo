def perfect(num):
	l=[]
	for x in range(1,num):
		if num%x==0:
			l.append(x)
	if sum(l) == num:
		print("prime")
	else:
		print("no")




perfect(7)