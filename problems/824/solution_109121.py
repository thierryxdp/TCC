def uppCons(string):
    """Funcao que recebe uma frase como entrada e retorna a mesma frase com todas as
    consoantes em maiusculas."""
   retorno = ''
	for caractere in string:
		if caractere.isupper():
			retorno += caractere.lower()
		else:
			retorno += caractere.upper()
	return retorno