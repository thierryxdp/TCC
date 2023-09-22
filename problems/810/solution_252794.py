def inverte(frase):
    '''
    funcao que dada uma frase, retorna outra frase que contem as
    mesmas palavras na ordem inversa, sem letras maiusculas e sem
    pontuaçao.
    :param frase: str
    :return: str
    '''
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