def freq_palavras(frases):
    '''
    função que recebe uma string e retorna um dicionário onde cada palavra 
    dessa string é uma chave e possui o valor do numero de vezes que a palavra aparece.
    str--->dict
    '''
    separador = frases.split()
    dicionario = {}

    for palavra in separador:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1

	return dicionario