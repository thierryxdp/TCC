def posLetra(string,letra,n):
    s1=[]
    s2=[]
    s3=[string]
    s4=[]
    i=0
    k=0
    a=''
    while i<len(string):
        s1.append(string[0+i:i+1])
        i=i+1
    if n>s1.count(letra):
        return -1
    else:
    	while letra in s1:
            s2.append([s1.index(letra)+k])
        	s1.remove(letra)
        	k=k+1
    	s4.append(s2[n-1])
        a+=str(s2[0])
        return a