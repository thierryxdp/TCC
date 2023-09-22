def filtra_pares(n):
    '''receba uma tupla com quatro elementos inteiros, e retorne uma nova tupla contendo apenas os elementos pares da tupla original'''
    '''int->int'''
    pares = ()
    
    for n in n:
        if n[0] %2 ==0:
            pares.append(n)
            
    return pares