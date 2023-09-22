def qtdFrasesTexto(texto):
    ''' '''
    exclamacao = texto.find('!')
    interrogacao = texto.find('?')
    reticencias = texto.find('...')
    pontof = texto.find('.')
    listaNova = [texto[:pontof + 1],texto[:exclamacao + 1],
	     texto[:interrogacao + 1], texto[:reticencias + 1]]
    return len(listaNova)