def freq_palavras(frases):
    '''função que calcula e retonra um dicionario com as palavras como chaves e a quantidade de vezes que ela aparece como valor;
    str -> dict'''
    lista1 = str.split(frases)
    palavras = []
    for p in lista1:
        palavras = palavras + [(p,list.count(lista1,p))]
    dic = dict(palavras)
    return dic