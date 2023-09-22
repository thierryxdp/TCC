def repetidos(lista_numeros):
    """retorna o número de vezes que um elemento da lista é igual ao elemento anterior;
    list -> int"""
    lista = lista_numeros
    contador = 0
    valor = 0
    valor2 = 1
    while contador < len(lista):
        if lista[valor] == lista[valor2]:
            valor = valor + 1
            valor2 = valor + 1
            contador = contador + 1
        else:
            valor = valor + 1
            valor2 = valor + 1
    return contador