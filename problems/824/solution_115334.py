def uppCons(frase):
    contador = 0
    nova_frase = ''
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxwyzBCDFGHJKLMNPQRSTVXWYZ':
            nova_frase = nova_frase + frase[contador].upper()
		else:
            nova_frase = nova_frase
        contador = contador + 1
        return nova_frase