def freq_palavras(frases):
    '''função que acaba retornando um dicionário onde mostra quantas vezes a palavra foi escrita; str => dic'''
    dic=0
    n=1
    lista=str.split(frases)
    for p in lista:
        if p in dic:
            dic[p]=dict.get(dic,p)+1
        else:
            dic[p]=1
    return dic