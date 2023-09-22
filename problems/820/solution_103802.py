def posLetra(frase, letra, ocorrencia):
    """Recebe uma frase, uma letra e um num de ocorrencia, 
    e retorna a posicao da string
    str, str, int --> int"""
    posicao = str.find(frase, letra, 0, ocorrencia)
    return posicao