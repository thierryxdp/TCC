def uppCons (frase):
    """Funçao que recebe uma frase e retorna a mesma com todas as consoantes maiusculas e seus demais caracteres 
    como na frase original"""
    lista=list(frase)
    proximo=0
    while proximo<len(lista):
        if lista[proximo] in 'bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ':
            lista[proximo]=str.upper(lista[proximo])
		proximo=proximo+1
	return ''.join(lista)