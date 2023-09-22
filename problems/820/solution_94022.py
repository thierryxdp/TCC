def posLetra(string, letra, ocorrencia):
    """ recebe uma string, uma letra e a ocorrencia desejada e retorna a posição da ocorrencia; str, str, int->int"""
    seguinte = 0
    lugar  = []
    
    if string.count(letra) < ocorrencia:
        return -1
    while seguinte < len(string):
        if string[seguinte] == letra:
            lugar.append(seguinte)
        seguinte = seguinte + 1
    return lugar[ocorrencia - 1]