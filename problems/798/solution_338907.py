def freq_palavras(frases):
    '''Retorna um dicionário onde cada palavra da string recebida
    seja uma chave e tenha como valor o número de vezes que a palavra aparece
    entrada: str
    saída: dicionário
    '''
    listapalavras=str.split(frases)
    dicionario={}
    for palavra in listapalavras:
        if palavra in list(dict.keys(dicionario)):
            dicionario[palavra]=dicionario[palavra]+1
        else:
            dicionario[palavra]=1
    return dicionario