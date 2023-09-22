def freq_palavras(frases):
    '''Uma função que receba uma string e retorne um dicionario 
    onde cada palavra dessa string seja uma chave e 
    tem como valor o numero de vezes que a palavra aparece.'''

    d = dict()
    for c in frases
      if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d