def uppCons(frase):
    """Função que recebe como entrada uma frase e retorne a frase com
    todas as suas consoantes em maiúsculas (e os demais caracteres
    exatamente como estavam na frase original).
    str -> str
    """
	i = 0
	frase_maiusculas = ''
	while i < len(frase):
		if frase[i] not in 'AEIOUaeiouãáâéêíîóôõúû':
			frase_maiusculas += frase[i].upper()
		else:
			frase_maiusculas +=frase[i]
		i = i+1
	return frase_maiusculas