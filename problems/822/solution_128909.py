def repetidos(lista):
    """ Retorna quantas vezes um elemento da lista é igual ao 
    elemento anterior"""
    R = 0 
    proximo = 0 
    ant = lista[1:len(lista)]
    while proximo < len(lista):
        if lista[n] == ant[n]:
            R = R + 1
    return R