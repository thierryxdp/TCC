def lingua_p(palavra):
    minuscula = palavra.lower()
    vogais = "aáàeéèíïìoóòuúù"
    for letra in vogais:
        minuscula = minuscula.replace(letra, letra + 'p' + letra)
    return minuscula