def uppCons(frase):
    """f"""
    contador = 0
    fraseformada = ''
    while contador < len(frase):
        if frase[contador] in 'AEIOUaeiou':
        fraseformada += str(frase[contador])
        if frase[contador] not in 'AEIOUaeiou':
            fraseformada += str(frase[contador]).upper
        contador += 1
	return fraseformada