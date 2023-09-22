def filtraMultiplos(lista,n):
    """Retorna uma lista contendo todos os elementos da lista original que forem divisiveis por n.
    lis,int->list"""
    i=0
    lista_final=[]
    while i<len(lista):
        if lista[i]%n==0:
            list.append(lista_final,lista[i])
        i+=1
    return lista_final