def freq_palavras(frases):
    '''Função que, dada uma frase qualquer, retorna a palavra
    da frase com o número de vezes que ela aparece, na forma
    de dicionário.
    str --> dict'''
    lista_frase = str.split(frases)
    palavras = []
    for palavra in lista_frase:
        palavras = palavras + [(palavra,list.count(lista_frase,palavra)),]
    dict_final = dict(palavras)
    return dict_final