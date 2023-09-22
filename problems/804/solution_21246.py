def filtra_pares(num):
    '''dada as variavel, ele calcula e retorna quais elementos da tupla são pares e os mantem em ordem em uma tupla. tup->tup'''
     r=[]
    for n in num:
        if n%2==0:
            r.append (n)
    r=tuple (r)
    print (r)
    return(r)