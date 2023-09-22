def freq_palavras(frase):
    ''' Esta fução recebe frase e retorna dicionáriocom a quantidade de de cada palavra da str.
    str--> dict'''
    palavras = frase.split()
    dicionario = {}
    cnt = 0
    for elementos in palavras:
        dicionario[palavras[cnt]] = palavras.count(palavras[cnt])
        cnt += 1
    return dicionario