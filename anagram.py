from collections import Counter

def cnt(s1,s2):
	if Counter(s1) == Counter(s2):
		print("anagaram")
	else:
		print("no")

def anagram(s1,s2):
	d1={};d2={}
	for x in range(len(s1)):
		d1[s1[x]]=s1.count(s1[x])
	for y in range(len(s2)):
		d2[s2[y]]=s2.count(s2[y])
	print(d1,d2)
	if d1 == d2:
		print("anagram")
	else :
		print("no anagaram")
cnt("evil", "vill")
anagram("evil", "vill")
