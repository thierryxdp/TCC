def filtraMultiplos(lista,n):
    '''retorna em uma lista todos os elementos que são
    díviseis por n; tem como entrada uma lista e um número;
    list,int->list'''
    lista_final=[]
    for elemento in lista:
        if elemento % n == 0:
            lista_final= lista_final.append(n)
    return lista_final