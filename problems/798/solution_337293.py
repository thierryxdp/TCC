def freq_palavras(frases):
    ''' Essa função tem como objetivo retornar um dicionario, contendo
    a quantidade de vezes que cada palavra foi escrita'''
    '''str->dict'''
    lista = str.split(frases)
    i = 0
    dicio= {}
    while i < len(lista):
        chave = lista[i]
        valor = list.count(lista, lista[i])
        dicio[chave] = valor
        i+=1
    return diciodef freq_palavras(frases):
    ''' Essa função tem como objetivo retornar um dicionario, contendo
    a quantidade de vezes que cada palavra foi escrita'''
    lista = str.split(frases)
    i = 0
    dicio= {}
    while i < len(lista):
        chave = lista[i]
        valor = list.count(lista, lista[i])
        dicio[chave] = valor
        i+=1
    return dicio