def maiores(lista,n):
    """Retorna uma nova lista que contenha todos os números da lista dada 
       maiores que n
       list,int->list
       Parametros:
       lista: uma lista qualquer
       n: um numero inteiro
    """
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)

    return lista[posicao+1:]