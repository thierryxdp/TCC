def freq_palavras(frases):
    '''função que retorna a quantidade de palavras de uma frase
    em um dicionário
    str->dict'''
    frase_separada=str.split(frases)
    dicio={}
    for palavra in frase_separada:
        repeticoes_palavra=str.count(frase_separada,palavra)
        dicio[palavra]=repeticoes_palavra
    return dicio