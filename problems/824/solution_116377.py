def uppCons(frase):
	'''Função que transforma as letras minusculas em letras maiusculas;
	string -> string'''
    i=0
    while i<len(frase):
        if frase[i]in 'abcdefghijklmnopqrstuvxyz':
            str.upper(frase[i])
        i = i + 1
		return frase