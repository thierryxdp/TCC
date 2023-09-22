def freq_palavras(frases):

    '''Função que recebe uma str e
    retorna a frequencia que seus itens aparecem.

    :param lista:str
    :return:dict'''

    a=0
    dicionario={}
    frases=str.split(frases)

    while a<len(frases):
        if frases[a] not in dicionario:
            dicionario[(frases[a])]=1
        else:
            dicionario[(frases[a])]= dicionario[(frases[a])]+1

        a=a+1

    return dicionario