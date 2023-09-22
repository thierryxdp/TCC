def filtraMultiplos(lista,n):
    '''recebe uma lista e um numero, e retorna uma lista com todos
       os numeros da lista que sao divisiveis pelo numero
       list -> list'''
    a=0
    b=len(lista)
    listaF=[]
    
    while a<b:
        if lista[a]%n=0.0:
            listaF=listaF+lista[a]
        a=a+1
    return listaF