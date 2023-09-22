def uppcons(frase):
    """Retornar uma função que receba uma frase e retorne a mesma com todas as suas consoantes maiúsculas; str=>str"""
	i=0
	frase1 = ''
	while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            frase1 = frase1 + str.upper(frase[i])
        else: 
            frase1 = frase1 + frase[i]
        i = i + 1
    return frase1