def freq_palavras(frases):
    '''recebe uma string e retorna um dicionário
    onde cada palavra da string dada é uma chave
    e tem como valor o número de vezes que a pala
    vra aparece.
    str -> dic
    '''
    dicionario = {}
    frase_sep = str.split(frases)
    for palavra in frases:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario