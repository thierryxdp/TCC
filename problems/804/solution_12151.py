def filtragem(a,b,c,d):
    'calcula e retorna apenas os elementros pares da tupla'
    'int,int,int,int->int,int,int,int'
    filtragem=[a,b,c,d]
    res=[]
    for n in filtragem:
        if n % 2==0:
            res.append(n)
            return(res)