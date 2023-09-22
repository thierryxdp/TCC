def freq_palavras(frases):
    '''recebe uma string e retorna um dicionario e a quantidade de vezes q essa palavra aparece. str->dict'''
    x={}
    stringfrase=str.split(frases)
    for n in stringfrase:
        if not n in x:
            x[n]=list.count(stringfrase,n)
    return x