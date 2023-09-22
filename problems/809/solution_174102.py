def intercala(lista1,lista2):
    """Funcao que recebe duas listas com tamanho 3 cada uma e gera uma terceira lista, que é
formada intercalando os elementos da lista 1 e da lista 2"""
    listaIntercalada = lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]
    return list(listaIntercalada)