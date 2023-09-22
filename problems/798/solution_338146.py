def freq_palavras(frases):
    '''
    função que recebe uma string e retorna um dicionario 
    onde cada palavra dessa string seja uma chave e tenha 
    como valor o numero de vezes que a palavra aparece 
    str -> dict
    '''
    palavras = frases.split()
    dicionario = {}
    for i in palavras:
        contador = palavras.count(i)
        dicionario.update({i:contador})
    return dicionario