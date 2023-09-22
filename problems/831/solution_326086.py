def lingua_p(palavra):
    lista=str.split(palavra)
    posicao=0
    for posicao in len(lista):
        if lista[posicao]=='aAeEiIoOuU':
            lista.insert(posicao+1,p)
            str.join(lista)
            posicao=posicao+1
    return lista