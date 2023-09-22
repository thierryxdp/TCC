def inverte(frase):
    '''funcao que rece uma frase e retorna as palavras da frase
    	na ordem inversa sem letras maiusculas e pontuacao
        travessao-> str
        virgula->str
        doisPontos->str
        Pvirgula->str
        final->str
        interrogacao->str
        exclamacao->str
    	fraseMinuscula->str
        fraseseparada ->str
        fraseinvertida->str
        return: str
    '''
	travessao = frase.replace('-', ' ')
	virgula = travessao.replace(',', ' ')
	doisPontos = virgula.replace(':', ' ')
	Pvirgula = doisPontos.replace(';', ' ')
	final = Pvirgula.replace('.', ' ')
	interrogacao = final.replace('?', ' ')
	exclamacao = interrogacao.replace('!', ' ')
    fraseMinuscula = str.lower(exclamacao)
    fraseseparada = frase_minuscula.split()
    fraseinvertida = frase_separada.reverse()
    return str.join(' ',frase_separada)