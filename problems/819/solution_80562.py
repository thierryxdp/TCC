def filtraMultiplos(lista,n):
    '''recebe uma lista e um numero, e retorna uma lista com todos
       os numeros da lista que sao divisiveis pelo numero
       list -> list'''
    a=1
    b=max(lista)
    listaF=[]
    
    while n*a<=b:
        if n*a in lista:
            listaF=listaF+[n*a]
        a=a+1
    return listaF