def maiores(lista,numero):
    # retorna uma lista com os numeros maiores que o numero inserido na lista
    lista.append(numero)
    lista.sort()
    posicao_numero = list.index(lista,numero)+1
    resultado = lista[posicao_numero:]
    return  (resultado)