def freq_palavras(frases):
    """A função recebe como entrada uma string e retorna
    um dicionário cujas chaves são as palavras contidas
    na string e os valores são as vezes em que a palavra
    aparece."""
    dicionario = {}
    palavras = frases.split()
    for palavra in palavras:
        ocorrencias = 0
        for aux in palavras:
            if palavra == aux:
                ocorrencias += 1
        dicionario[palavra] = ocorrencias
    return dicionario