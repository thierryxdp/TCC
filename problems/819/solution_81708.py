def filtra_multiplos(lista,x):
    """ Função que dada uma lista de números inteiros e um número avulso, retorna a lista com os elementos que forem divisíveis pelo número avulso
    list,int -> list """
    i=0
    lista_multiplos=[]
    while i<len(lista):
        if lista[i]%x==0:
            list.append(lista_multiplos,lista[i])
        i=i+1
    return lista_multiplos