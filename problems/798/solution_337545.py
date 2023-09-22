def freq_palavras(frases):
    """Função que define quantas vezes uma palavra aparece dentro de uma frase;
    str -> dict"""
    X = frases.split((' '))
    final = {}
    for palavra in X:
        ocorrencia = list.count(X, palavra)
        final[str(palavra)] = ocorrencia
    return final