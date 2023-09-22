def maiores(lista_com_numeros,n):
    """dada uma lista de números inteiros e um número inteiro n, retorna outra lista que contém todos os
    números da lista original maiores que n  (list[int,int,...,int],int --> list[int,int,...,int])""" """
    a função funciona quando os números de entrada (tanto os da lista quanto o valor n) são do tipo float,
    porém a função não lida com o tipo complex"""
    lista_com_n = lista_com_numeros + [n] #nesta etapa, insere-se o número n na list
    list.sort(lista_com_n) #nesta etapa, ordena-se a lista que já possui o número n incluso
    posicao_de_n = list.index(lista_com_n,n) #aqui se descobre o posicionamento do número n na lista ordenada
    return lista_com_n[posicao_de_n+1:] #finalmente, retorna-se a lista ordenada com todos os números da lista orginal maiores que n