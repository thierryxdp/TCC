def posLetra (string, letra, numero):
    """Retorna a posição da string em que a letra da entrada está (segundo sua ocorrencia indicada em número; 1= primeira ocorrência, 2= segunda ocorrência, etc...);. str, str, int-> int)"""
    x=0
    while x <= len(string):
        if letra in string