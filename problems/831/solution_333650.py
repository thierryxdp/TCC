def lingua_p(palavra):
    vogais = ['a','e','i','o','u','á','é','í','ó','ú']
    palavra = str.lower(palavra)
    resultado = []
    x = 0
    while x < len(palavra):
        resultado.append(palavra[x])
        if palavra[x] in vogais:
            resultado.append('p')
            resultado.append(palavra[x])
		x += 1 
    return ''.join(resultado)