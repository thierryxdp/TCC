def lingua_p(palavra):
    palavra = str.lower(palavra)
	vogais = ['a','e','i','o','u','á','é','í','ó','ú']
    resultado = []
    for letra in palavra:
        resultado.append(letra)
        if letra in vogais:
            resultado.append('p')
            resultado.append(letra)
    return ''.join(resultado)