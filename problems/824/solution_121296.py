def uppCons(frase):
    alfabeto = 1
    frase_final = frase[0].upper()
    while alfabeto < len(frase):
        if frase[alfabeto] in ('b','c','ç','d','f','g','h',
                               'j','k','l','m','n','p','q',
                               'r','s','t','v','w','x','y',
                               'z','B','C','Ç','D','F','G',
                               'H','J','K','L','M','N','P',
                               'Q','R','S','T','V','W','X',
                               'Y','Z'):
            frase_final += frase[alfabeto].upper()
        else:
            frase_final += frase[alfabeto].lower()
        alfabeto += 1
	return frase_final