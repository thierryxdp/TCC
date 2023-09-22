def lingua_p(palavra):
    posicao=0
    for posicao in range(palavra):
        lista=str.split(palavra)
        if lista[posicao]=='aAeEiIoOuU':
            lista.insert(posicao+1,p)
            str.join(lista)
    return lista