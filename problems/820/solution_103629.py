def posLetra(string, letra, numero):
    """
    funçao que dada uma string, uma letra e um numero, retorna a
    posiçao da string aquela ocorrência da letra esta.
    :param string: str
    :param letra: str 
    :param numero: int 
    :return: int
    """
    contador = 0
    indice = 0
    ocorrencia = 0
    lista = list(string)
    while contador < len(lista):
        if lista[indice] == letra:
            ocorrencia += 1
            if ocorrencia == numero:
                return indice

        contador += 1
        indice += 1

    return -1