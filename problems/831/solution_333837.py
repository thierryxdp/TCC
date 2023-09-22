def lingua_p(palavra):
    minuscula = palavra.lower()
    vogais = "aáeéiíoóuú"
    for letras in vogais:
        minuscula = minuscula.replace(letra, letra + 'p' + letra)
        return minuscula