def insere(lista_numero,n):
    """Dado uma lista em ordem crescente de números inteiros e um número (n), a função insere inclui (n) na posição
    correta, ou seja, de modo que a lista siga ordenada  (list[int,int,...,int],int --> list[int,int,...,int])""" """
    Caso uma lista seja entregue contendo algum número float e/ou a lista seja desordenada, a função ainda entregará
    uma lista propriamente ordenada. Todavia, caso seja inserido alguma lista contendo um complex ou algum (n) complex,
    a função não funcionará"""
    lista_com_numero_n = lista_numero + [n] #nessa etapa, adiciona-se o elemente n à lista
    list.sort(lista_com_numero_n) #nessa etapa, ordena-se a lista que já possui o elemento n
    return lista_com_numero_n #retorna-se a lista ordenada e possuidora do elemento n