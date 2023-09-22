def uppCons(frase):
    vogais = {'a', 'e', 'i', 'o', 'u',
             'á', 'é', 'í', 'ó', 'ú',
             'â', 'ê', 'î', 'o', 'û',
             'ã', 'õ'}
    for letra in frase:
        if letra not in vogais:
            frase = frase.replace(letra, letra.upper(), 1)
    return frase