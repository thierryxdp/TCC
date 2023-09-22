def uppCons(frase):
    maiusculas=''
    vogais ='aeiouáéíóúâêîôûãõ'
    for letra in frase:
        if letra.lower() not in vogais:
            maiusculas+=letra.upper()
        else:
            maiusculas+=letra
    return maiusculas