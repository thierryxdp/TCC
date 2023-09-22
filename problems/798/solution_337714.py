def freq_palavras(frases):
     '''
    Funcao que recebe uma string. A funcao retorna um dicionario onde cada palavra da string de entrada
    e uma chave e tenha como valor o numero de vezes que a palavra aparece
    str -> int
    '''  
    chaves = frases.split()
    dic = {}
    for chave in chaves:
        if chave in dic.keys():
            dic[chave] = dic[chave] + 1
        else:
            dic[chave] = 1
    return dic