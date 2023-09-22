def posLetra(string, letra, ocorrencia):
    seguinte = 0
    lugar = []
    
    if frase.count(string, letra) < ocorrencia:
        return -1
    while seguinte < len(string):
        if string[seguinte] == letra:
            posicao.append(seguinte)
        seguinte = seguinte + 1
    return lugar[ocorrencia - 1]