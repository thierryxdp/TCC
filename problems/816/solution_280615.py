def maiores(lista,numero):
    lista.append(numero)
    lista.sort()
    posicao_numero = list.index(lista,numero)+1
    resultado = lista[posicao_numero:]
    
    return  resultado