def test(l):
	s=""
	for x in l:
		s=s+str(x)
	print(s)
	l=[x for x in s]
	print(l)
	for x in range(len(l)):
	 	for y in range(len(l)):
	 		if l[x]>l[y]:
	 			l[x],l[y]=l[y],l[x]
		
		

	print("".join(l))
	



test([10,2,12,98,67])