def conta_frases(frase):
    """conta o número de frases no texto"""
    ocorrencia = 0
    ocorrencia +=  + str.count(frase,'!') + str.count(frase,'?') +str.count(frase,'...')
    return ocorrencia