def uppCons(frase):
    vogais = {'a', 'e', 'i', 'o', 'u'}
    for letra in frase:
        if letra not in vogais:
            frase.replace(letra, letra.upper())
    return frase