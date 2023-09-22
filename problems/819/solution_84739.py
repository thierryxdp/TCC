def filtraMultiplos(lista,n):
    """Função que retorna uma lista contendo todos os números divisíveis
por um número n; list,int -> list"""
    lista_filtrada=[]
    cont = 0
    while cont<len(lista):
        if lista[cont]%n==0:
            lista_filtrada+=[lista[cont]]
            cont+=1
        else:
            cont+=1
    return lista_filtrada