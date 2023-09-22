def uppCons(frase):
    maiusculas=''
    vogais ='aeiouáéíóúâêîôû'
    for letra in frase:
        if letra not in vogais:
            maiusculas+=letra.upper()
    return maiusculas