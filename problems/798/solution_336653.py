def freq_palavras(frases):
    '''recebe uma ou mais frases e retorna um dicionario onde cada chave
    é uma palavra da frase e o valor de cada chave é a quantidade
    de vezes que a palavra aparece;
    str->dict'''
    frases=str.split(frases)
    palavras={}
    for palavra in frases:
        if palavra in palavras:
            palavras[palavra]+=1
        else:
            palavras[palavra]=1
    return palavras