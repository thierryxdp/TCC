def inverte(frase):
    '''função que dada uma frase retorna ela escrita na ordem inversa,
    sem letras maiúsculas e sem pontuação
    str->str'''
    
    travessao = frase.replace('-', ' ')
	virgula = travessao.replace(',', ' ')
	dois_pontos = virgula.replace(':', ' ')
	ponto_virgula = dois_pontos.replace(';', ' ')
	ponto_final = ponto_virgula.replace('.', ' ')
	ponto_interrogacao = ponto_final.replace('?', ' ')
	ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    frase_minuscula = str.lower(ponto_exclamacao)
    frase_separada = frase_minuscula.split()
    frase_invertida = frase_separada.reverse()
    return str.join(' ',frase_separada)