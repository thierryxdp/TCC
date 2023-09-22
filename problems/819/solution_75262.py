def filtraMultiplos(lista_de_numero, n):
    '''Função que filtra os múltiplos de um número, retorna outra lista contendo
       todos os elementos da lista originalque eorem divisíveis por n.
       lista,int ---> lista'''
    nova_lista = []
    num = 0
    while num < len(lista_de_numero):
        if lista_de_numero[num] % n == 0:
            nova_lista.append(lista_de_numero[num]) 
        num = num + 1
    return nova_lista