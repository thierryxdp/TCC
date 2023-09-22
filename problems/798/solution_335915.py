def freq_palavras(frases):
    '''
    recebe uma string e retorna um dicionário onde cada
    palavra da entrada é uma chave que te como valor o numero
    de vezes que a palavra aparece
    str->dict
    '''
    lista_palavras=str.split(frases)
    dicionario={}
    for i in lista_palavras:
        if i in dicionario:
            dicionario[i]=dict.get(dicionario,i)+1
        if i not in dicionario:
            dicionario[i]=1
    return dicionario