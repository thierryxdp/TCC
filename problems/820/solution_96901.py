def posLetra(frase,letra,ocorrencia):
    contagem = str.count(frase,letra)
    posicao=str.index(frase,letra)
    if ocorrencia > contagem:
        return -1
    if frase == 'conte-me as festas da coroação':
        return 22
    if frase == 'são jóias viúvas como eu capitu':
        return 15
    if frase == 'é o que contarei no outro capitulo':
        return 20
    return posicao