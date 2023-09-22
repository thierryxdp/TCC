def posLetra(str, l, n):
    """
    funçao que dada uma string, uma letra e um numero, retorna a
    posiçao da string aquela ocorrência da letra esta.
    :param n(numero): int
    :param str: str 
    :return: int
    :param l(letra): str
    """
  
    indice = 0
    ocorrencia = 0
    cont = 0
    lista = list(str)
    
    while cont < len(lista):
        if lista[indice] == l:
            ocorrencia += 1
            if ocorrencia == n:
                return indice

        contador += 1
        indice += 1
    else:  
        return -1