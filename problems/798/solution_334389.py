def freq_palavras (frase):
    '''recebe uma string e retorna um dicionario com o número de vezes em que essa palavra aparece'''
    '''str->dicionario'''
    i = 0
    final = {}
    for nome in frase:
        if nome [i] in frase:
            um = frase.count(nome)
        i = i+1
    return um