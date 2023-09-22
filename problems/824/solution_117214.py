def uppCons(frase):
    '''Função que dada uma frase qualquer, retornará todas as consoantes da frase em maiúsculo,
    e os demais caracteres sem alteração.
    frase - > str
    return -> str'''
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    i = 0
    frase_pronta = frase
    while i < len(frase):
        if frase[i] in consoantes:
            frase_pronta = frase_pronta.replace(frase_pronta[i], frase_pronta[i].upper())
        i+= 1
	return frase_pronta