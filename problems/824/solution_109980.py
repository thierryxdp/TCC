def uppCons(frase):
    """A Função filtra a frase e retorna a frase com as letras
	(Exceto as vogais) em maíuscula; str->str"""
    maiuscula=''.join(letra.upper() if letra in 'bcdfghjklmnpqrstvwxzç' else letra for letra in frase)
    return maiuscula