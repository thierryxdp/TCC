def uppCons(frase):
    maiusculas=''
    vogais ='aeiouáéíóúâêîôû'
    for letra in palavra:
        if letra not in vogais:
            letra.upper()
            maiusculas+=letra
    return maiusculas