def bubble(s):
	l=list(s)
	for x in range(len(l)):
		for y in range(0,len(l)-x-1):
			if l[y] > l[y+1]:
				l[y] , l[y+1] = l[y+1], l[y]
	return "".join(l)




result=bubble("abdc123ju3")
print(result)

