def freq_palavras(frases):
    '''Esta função retorna quantas vezes uma palavra se repete na frase.
    str >>>dict '''
    lista = str.split(frases)
    i = 0
    dicionario = {}
   
    while i < len(lista):
        palavra = lista[i]
        dicionario[palavra] = list.count(lista, palavra)
        i += 1
        
	return dicionario