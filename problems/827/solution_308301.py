def qtd_divisores(n:int)->list:
    '''Devolve os divisores do número e quantos divisores ele tem no total'''
    i=1
    a=[]
    if n<1:
        '''número negativo tem 0 divisores sempre'''
        return 0
    while i<=n:
        if n%i==0:
            a.append(i)
        i+=1
    b=str(a)
    return b.count(',')+1