def filtraMultiplos(lista_de_numero, num):
    '''Função que filtra os múltiplos de um número, retorna outra lista contendo
       todos os elementos da lista originalque eorem divisíveis por n.
       lista,int ---> lista'''
    nova_lista = []
    num = 0
    while num < len(nova_lista):
        if lista[num] * num == 0:
            nova_lista = nova_lista + nova_lista[num]
            num = num + 1
    return nova_lista