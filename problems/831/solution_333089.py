def lingua_p(palavra):
    minuscula = palavra.lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    for letra in vogais:
        minuscula = minuscula.replace(letra, letra + 'p' + letra)
    return minuscula