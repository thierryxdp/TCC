def qtd_divisores(n):
    ListaA=[]
    i=n
    
    for i range(1,n+1):
        if i%i==0:
            ListaA.append(i)
            
            return len(ListaA)