def ss(s1,s2):
	l=len(s2)
	cnt=0
	for x in range(len(s1)-l+1):
		
		if s1[x:x+l] == s2:
		 	cnt+=1
	return cnt



c=ss("cdcabcaadcdc","a")
print(c)