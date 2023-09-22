def freq_palavras(frases):
    '''Esta função retorna quantas vezes uma palavra se repete na frase.
    str >>>dict '''
    lista = str.split(frases)
    dicionario = {}
   
    while i < len(lista):
        chave = lista[i]
        valor = list.count(lista, [i])
        dicio[chave] = valor
        
        return dicio