def posLetra(x,y,z):
    """ Recebe uma string e um número que indica a ocorrência
    desejada da letra, e retorna em que posição da string aquela 
    ocorrência da letra está.
    assinatura: str, str, int--> int
    """
    if x.count(y) < z:
        return -1
    if x.count(y) >= z:
        return x.find(y)