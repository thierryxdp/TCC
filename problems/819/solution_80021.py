def filtraMultiplos(lista,n):
    """dada uma lista e um numero n, retorna os
    numeros dessa lista que sao multiplos de n
    list,int-->list"""
    filtrados=[]
    count=0
    lista_copy=lista[:]
    while count < len(lista_copy):
        if lista[count]%n==0:
            filtrados=filtrados+[lista[count]]
        count=count+1
    return filtrados