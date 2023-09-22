def lingua_p(palavra):
    vogais = ['a','e','i','o','u']
    resultado = []
    for letra in palavra:
        resultado.append(letra)
        if letra in vogais:
            resultado.append('p')
            resultado.append(letra)
    return ''.join(resultado)