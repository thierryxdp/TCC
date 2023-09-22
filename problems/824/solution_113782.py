def uppCons (frase):
    """ transforma todas as consoantes da frase em maiúsuclas"""
    qtd = len (frase)
    indice = 0
    while indice < qtd:
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            str.upper (frase[indice])
		indice += 1
	return frase