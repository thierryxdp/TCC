def qtd_divisores(n:int)->list:
    '''Devolve os divisores do número e quantos divisores ele tem no total'''
    i=1
    a=[]
    while i<=n:
        if n%i==0:
            a.append(i)
        i+=1
    return a