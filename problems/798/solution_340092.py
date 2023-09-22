def freq_palavras(texto):
    """Função que, dado um texto, verifica a frequência com que as palavras se repetem. str -> dict"""
    frequencia = {}
    texto = texto.split()
    for t in range(len(texto)):
        if texto[t] in frequencia:
            frequencia[texto[t]] += 1
        if texto[t] not in frequencia:
            frequencia[texto[t]] = 1
    return frequencia