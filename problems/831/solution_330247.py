def lingua_p(palavra):
    palavra_com_p = ''
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    for letras in palavra:
        if str.lower(letras) not in consoantes:
            troca = letras + 'p' + letras
            palavra_com_p += troca
		if str.lower(letras) in consoantes:
            palavra_com_p += letras
	return palavra_com_p