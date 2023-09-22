resultado = []
def lingua_p(palavra):
    vogais = ['a','e','i','o','u']
    final = []
    for letra in palavra:
        resultado.append(letra)
        if letra in vogais:
            resultado.append('p')
    return ''.join(resultado)