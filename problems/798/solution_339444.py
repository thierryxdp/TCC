def freq_palavras(frases):
    '''Essa função conta o número de vezes que uma palavra aparece em 
    uma frase
    
    str->dict'''
    
    lista_palavras = frases.split()
    dicionario = dict.fromkeys(lista_palavras,0)
    for contador in range(len(lista_palavras)):
        dicionario[lista_palavras[contador]] += 1
    return dicionario