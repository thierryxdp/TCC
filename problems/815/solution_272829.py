def insere (lista_numeros,n):
    """ Função que, dadas uma lista ordenada crescente de numeros inteiros(lista_numero)
    e um numero inteiro n, retorna a lista dada com o numero n inserido na posição correta segundo 
    a ordem crescente
    list,int-> list"""
    list.insert (lista_numeros,n,n)
    list.sort(lista_numeros)
    return lista_numeros