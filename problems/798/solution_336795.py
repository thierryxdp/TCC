def freq_palavras(frases):
    '''
	recebe uma string e retorna um dicionário onde cada palavras dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece;
    str -> dic
    '''
	string = frases.split
    dicionario = {}
    i = 0
    for string in frases:
        if string[i] not in frases:
            dicionario + {string[i]:1}
            else:
            dicionario + {string[i]:2}
        i = i + 1
        return dicionario