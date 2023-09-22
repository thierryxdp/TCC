def quant_palavras(frase):
    '''Conta a quantidade de palavras por frase. Str->Int'''
    qnt = 0
    i = 0
    frase = str.split(frase)
    while i < len(frase):
        qnt = qnt + list.count(frase[i])
    return qnt