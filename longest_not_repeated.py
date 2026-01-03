def test(s):
    l=[]
    for x in range(len(s)):
        value=s[x]
        for y in range(x+1,len(s)):
            if s[y] not in value:
                value=value+s[y]
               
            else:
                l.append(value)
                break

        else:
            l.append(value)
           
    
    return l
l=test("abcdedfddd")
if len(l)==0:
    print("empty string")
else:
    print(max(l,key=len))

















































