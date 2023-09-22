def freq_palavras(frases):
    '''Esta função retorna quantas vezes uma palavra se repete na frase.
    str >>>dict '''
    lista = str.split(frases)
    i = 0
    dicionario = {}
   
    while i < len(lista):
        valor = list.count(lista, [i])
        dicionario[lista[i]] = valor
        i += 1
        
        return dicionario