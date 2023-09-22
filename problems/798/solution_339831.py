def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionario no qual cada palavra seja chave e tenha como valor quantas vezes ela aparece'''
    palavras = frases.split()
    dicionario={}
    for i in palavras:
        contador=palavras.count(i)
        dicionario.update({i: contador})
    return dicionario