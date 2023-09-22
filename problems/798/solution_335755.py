def freq_palavras(palavra):
    ocorrencias = {}
    for c in palavra:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrencias