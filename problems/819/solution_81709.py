def filtra_Multiplos(lista,x):
    """ Função que dada uma lista de números inteiros e um número avulso, retorna a lista com os elementos que forem divisíveis pelo número avulso
    list,int -> list """
    i=0
    lista_Multiplos=[]
    while i<len(lista):
        if lista[i]%x==0:
            list.append(lista_Multiplos,lista[i])
        i=i+1
    return lista_Multiplos