def uppCons(frase):
    '''funcao que retorna a frase de entrada com todas as suas consoantes em maiusculo,
    enquanto os demais caracteres retornam iguais a como estavam originalmente.
    string -> string'''
    consmaiuscula = ''
    caractere = 0
    consoantes = 'BCÇDFGHJKLMNPQRSTVWXYZbcçdfghjjklmnpqrstvwxyz'
    while caractere<len(frase):
		if frase[caractere] in consoantes:
			consmaiuscula = consmaiuscula + str.upper(frase[caractere])
		else:
			consmaiuscula = consmaiuscula + frase[caractere]
		caractere= caractere+1
	return consmaiuscula