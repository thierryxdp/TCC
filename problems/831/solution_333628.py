resultado = []
def lingua_p(palavra):
    vogais = ['a','e','i','o','u']
    final = []
    for letra in palavra:
        if letra in vogais:
            resultado.append('p')
        resultado.append(letra)
    return ''.join(resultado)