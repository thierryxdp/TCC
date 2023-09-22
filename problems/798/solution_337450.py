def freq_palavras(frases):
    '''Esta função retorna quantas vezes uma palavra se repete na frase.
    str >>>dict '''
    lista = str.split(frases)
    i = 0
    dicionario = {}
    
    while i < len(lista):
        chave = lista[i]
        valor = list.count(lista,lista[i])
        dicionario[chave] = valor
        i+=1
        
    return dicionario