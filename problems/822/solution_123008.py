def repetidos(lista):
    """ Funçao que recebe uma lista numérica  e retorna quantas vezes um elemento da lista se repetiu.
    list - int  """
    ind= 0
    c = 0
    repete = 0
    while c < len(lista):
        if lista[ind] == lista[ind - 1]:
          	repete += 1

        ind += 1
        c += 1

    return repete