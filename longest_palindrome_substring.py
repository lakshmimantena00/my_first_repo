def test(s):
    l=[]
    for x in range(len(s)):
       
        for y in range(x+1,len(s)+1):
            value=s[x:y]
            if value == value[::-1]:
                l.append(value)
    print(l,"is the list")
    
    return (max(l,key=len))
     
    
l=test("cbbd")
print(l)

















































