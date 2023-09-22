def maiores (inteiros,n):
    '''retorna outra lista com os numeros da original em ordem crescente maiores que n'''
    '''list,int -> list'''
    
    
    maiores=list()
    lista.sort()
    for c in inteiros:
        if c >= n:
            maiores.append(c)
            return maiores