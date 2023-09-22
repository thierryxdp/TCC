def lingua_p(palavra):
    palavra_com_p = ''
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    for letras in palavra:
        if str.lower(letras) not in consoantes:
            troca = letra + 'p' + letra
            palavra_com_p += troca
		if str.lower(letras) in consoantes:
            palavra_com_p += letra
	return palavra_com_p