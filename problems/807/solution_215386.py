def conta_frases(texto):
    '''função que retorna o número de frases contidas no texto
    str -> int'''
    lista1 = str.split(texto,'...')
    for conteudo in lista1:
        lista2 = str.split(conteudo, '.')
	for conteudo in lista2:
        lista3 = str.split(conteudo, '!')
    for conteudo in lista3:
        lista4 = str.split(conteudo, '?')
    return len(lista4)