def freq_palavras(frases):
    '''Função que  recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que ela aparece.
    str -> dict'''
    palavras = frases.split()
    dicio = {}
    for i in palavras:
        conta_palavras = palavras.count(i)
        dicio.update({i: conta_palavras}) 
    return dicio