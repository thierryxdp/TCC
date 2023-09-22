def repetidos(lista_numeros):
    """retorna o número de vezes que um elemento da lista é igual ao elemento anterior;
    list -> int"""
    lista = lista_numeros
    contador = 0
    valor = 0
    valor2 = 1
    retorno = []
    while contador < len(lista):
        if lista[valor] == lista[valor2]:
            list.append(retorno, lista[contador])
            valor = valor + 1
            valor2 = valor + 1
            contar = contar + 1
    return retorno