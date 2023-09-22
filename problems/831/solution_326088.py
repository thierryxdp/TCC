def lingua_p(palavra):
    posicao=0
    for posicao in range(len(lista)):
        if lista[posicao] in 'aAeEiIoOuU':
            lista.insert(posicao+1,p)
            str.join(lista)
            posicao=posicao+1
    return lista