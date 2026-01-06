def test(s1,s2):
	l=len(s2)
	for x in range(len(s1)):
		
		if s1[x:x+l] == s2:
			return x
		

	return -1


val=test("ramaswamyz","yz")
print(val)