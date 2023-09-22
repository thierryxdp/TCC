def filtra_pares (tup):
    '''funcao que retorna uma tupla apenas com os elementos pares da tupla dada
    tuple(int) -> tuple(int)'''
    a= int(tup[0])%2
    b= int(tup[1])%2
    c= int(tup[2])%2
    d= int(tup[3])%2
    
    if a+b+c+d==0:
        return tup
    elif a+b+c+d!=0:
        return ()