def primo(n):
    i=1
    lista=[1,2,3,5,7]
    lista2=[]
    for c in range(1,n+1):
        while i<=n:
        	if c%lista[i]==0:
                lista2.append(c)
                i+=1
            else:
                i+=1
        if len(lista)==n:
            return True
        else:
            return False