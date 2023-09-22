def lingua_p(palavra):
    ''' retorna a palavra traduzida para a língua P, dado como parâmetro uma palavra(em português);
    str -> str '''
    m = palavra.lower
    n = ''
    vogais = 'aeiouàáâãéêíóúõô'
    for elem in m:
        n = n+elem
        if elem in vogais:
            n = n+ 'elem' + elem
	return n