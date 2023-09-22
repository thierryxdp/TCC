def filtraMultiplos(lista,n):
    """dado uma lista de números e um número, a funcão retorna outra lista contendo
    todos os elementos que forem divisíveis pelo número n;
    list,int->list"""
    listanova=[]
    ultimo=lista[-1]
    indice= 0
    while lista[indice]<= ultimo:
        if lista[indice]%n==0:
            list.append(listanova,lista[indice])
    return listanova