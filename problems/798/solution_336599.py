def freq_palavras(frases):
    '''função que recebe uma string,frases, e retorna um dicionário com a palavra da string e seu número de ocorrências na string'''
    fr={}
    pa= frases.split()
    for i in pa:
        if i in fr:
            fr[i]=fr[i]+1
        else:
            fr[i]=1
    return fr