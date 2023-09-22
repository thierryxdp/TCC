def insere(lista_numeros,n):
    """funcao que dado uma lista crescente de numeros inteiros e um numero inteiro n, 
    retorna uma nova lista que inclui n na posicao correta, de modo que a lista continue ordenada;
    list, int -> list"""
    variavel=lista_numeros
    variavel+=[n]
    return list.sort(variavel)