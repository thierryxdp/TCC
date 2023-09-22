def posLetra(string, l, ocorrencia):
    """
    str,str,int->int
    :param string: Recebe de entrada uma string
    :param 1: Recebe uma letra
    :param ocorrencia: Indica a ocorrencia da letra(l)
    :param return: Retorna a posição da String naquela ocorrencia da letra.
    """
    if str.count(string,l) < ocorrencia:
        return -1
    contador = ocorrencia
    indice = 0
    while indice < len(string):
        if l == string[indice] and contador == 1:
            return indice
        elif l == string[indice]:
            contador = contador - 1
        indice = indice +1