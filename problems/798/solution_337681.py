def freq_palavras(frases):
    ''' Recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave e mostre quantas vezes essa palavra aparece'''
    frases_lista=frases.split(" ")
    dicionario={}
    for i in frases_lista:
        if not i in dicionario.keys():
            dicionario[i]=1
        else:
            dicionario[i]=dicionario[i] + 1
    return dicionario