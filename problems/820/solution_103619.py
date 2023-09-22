def posLetra(str, l, n):
    """
    funçao que dada uma string, uma letra e um numero, retorna a
    posiçao da string aquela ocorrência da letra esta.
    :param string: str
    :param letra: str 
    :param numero: int 
    :return: int
    """
  
    indice = 0
    ocorrencia = 0
    cont = 0
    lista = list(str)
    
    while cont < len(l):
        if lista[indice] == l:
            ocorrencia += 1
            if ocorrencia == n:
                return indice

        cont += 1
        indice += 1

    return -1