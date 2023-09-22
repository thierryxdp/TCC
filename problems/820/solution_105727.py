def posLetra(string,letra,n):
    s1=[]
    s2=[]
    s3=[string]
    i=0
    k=0
    while i<len(string):
        s1.append(string[0+i:i+1])
        i=i+1
    while letra in s1:
        s2.append([s1.index(letra)+k])
        s1.remove(letra)
        k=k+1
    return s2[n-1]