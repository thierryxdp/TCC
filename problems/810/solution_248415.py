def inverte(frase):
    '''
   função que dada um afrase retorna uma outra frase com as mesmas 
   palavras, mas ordem inversa,s em letras maiusculas e sem pontuação
    
    '''
	
	virgula = frase.replace(',', ' ')
	dois_pontos = virgula.replace(':', ' ')
	ponto_final =dois_pontos.replace('.', ' ')
	ponto_interrogacao = ponto_final.replace('?', ' ')
	ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    travessao = ponto_exclamacao .replace('-', ' ')
    ponto_virgula = travessao.replace(';', ' ')
   
    
    frase_minuscula = str.lower(ponto_exclamacao)
    frase_separada = frase_minuscula.split()
    frase_invertida = frase_separada.reverse()
    return str.join(' ', frase_separada)