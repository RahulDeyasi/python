def solve(s):
    str1=list(s.split())
    m=list()
    for i in str1:
        strr=i
        str2=i.lower()
        str3=str2[::-1]
        if str2==str3:
            m.append(strr)
    print(max(m))
s=input()
solve(s)
        
