def freq_palavras(frases):
    '''calcula uma funcao que recebe uma string e retorna um dicionario
    onde cada palavra dessa string é uma chave e tenha como valor o numero
    de vezes que a palavra aparece;
    str-->dict.'''
    dic = {}
    frases = str.split(frases)
    for i in range(len(frases)):
        cont = frases.count(frases[i])
        if i < len(frases):
            dic[frases[i]] = cont
    return dic