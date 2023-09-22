def uppCons (frase: str) -> str:
    """Recebe uma frase e retorna a mesma frase com todas consoantes em maiúscula
    e os demais caracteres na forma original."""
    frase_auxiliar = ''
    tamanho_da_frase = len(frase)
    contador = 0
    while contador < tamanho_da_frase:
        if str.lower(frase[contador]) in 'bcdfghjklmnpqrstvxwyz':
            frase_auxiliar += str.upper(frase[contador])
    	else:
    	    frase_auxiliar += frase[contador]
    	contador += 1
	return frase_auxiliar