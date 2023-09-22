def freq_palavras(frase):
    """Função recebe uma frase e retorna a frequencia com que as palavras aparecem na mesma.
    str -> dict"""
    frequencia = {}
    frase = frase.split()
    for i in range(len(frase)):
        if frase[i] in frequencia:
            frequencia[frase[i]] += 1
        if frase[i] not in frequencia:
            frequencia[frase[i]] = 1
    return frequencia