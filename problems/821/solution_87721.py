def fatorial(numero):
    '''Calcula o fatorial do número recebido
    int-> int'''
    lista = list(range(1,numero + 1))
    lista2 = list.reverse(lista)
    produto = 0
    indice = 0
    while indice < (len(lista) - 1) :
        produto = lista[indice] * lista[indice+1]
        lista[indice+1] = produto
        indice += 1
    return produto