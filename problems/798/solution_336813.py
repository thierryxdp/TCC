def freq_palavras(frases):
    '''
	recebe uma string e retorna um dicionário onde cada palavras dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece;
    str -> dic
    '''
	dicionario = {}
    str_separada = frases.split()
    for plv in str_separada:
        if plv not in dicionario:
            dicionario[plv] = 0
        dicionario[plv] = dicionario[plv] + 1
        
        
    return dicionario