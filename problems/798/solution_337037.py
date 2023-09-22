def freq_palavras(frases):
    ''' retorna um dicionário com todas as palavras da frase e a quantidade de vezes
    que ela se repete dentro da frase. str->dicio'''
    lista_frases= frases.split()
    dicio={}
    for i in lista_frases :
        if i in dicio:
            dicio[i]+=1
        else:
            dicio[i]=1
    return dicio