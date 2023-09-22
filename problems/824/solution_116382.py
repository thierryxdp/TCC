def uppCons(frase):
	'''Função que transforma as letras minusculas em letras maiusculas;
	string -> string'''
    return ''.join(caractere.upper() if caractere in 'bcdfghjklmnpqrstvxwyz' else caractere for caractere in frase)