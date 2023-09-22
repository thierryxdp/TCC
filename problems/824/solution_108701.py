def uppCons(frase):
    """Função que recebe uma frase e retorna a frase com todas as suas consoantes
    em maiusculas.
    str -> str."""
    contador = 0
    fraseFinal = frase
    while contador < len(frase):
        if frase[contador] not in 'AEIOUaeiou':
            str.replace(fraseFinal, frase[contador], str.upper(frase[contador]))
		contador = contador + 1
	return fraseFinal