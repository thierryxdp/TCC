def inverte(frase):
    '''
    função que dada uma frase, retorna outra frase com as mesmas palavras, 
    mas na ordem inversa, sem letras maiusculas e sem pontuação. FRASE---> STR RETURN--->STR
    '''
	travessao = frase.replace('-', ' ')
	virgula = travessao.replace(',', ' ')
    ponto_virgula = virgula .replace(';', ' ')
    dois_pontos = ponto_virgula.replace(':', ' ')
	ponto_final = dois_pontos.replace('.', ' ')
	ponto_interrogacao = ponto_final.replace('?', ' ')
	ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    frase_minuscula = str.lower(ponto_exclamacao)
    frase_separada = frase_minuscula.split()
    frase_invertida = frase_separada.reverse()
    frase_separada = frase_invertida.split()
    ponto_interrogacao = frase_separada .replace('?', ' ')
    return str.join(' ',ponto_interrogacao )