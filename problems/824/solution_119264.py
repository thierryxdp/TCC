def uppCons(frase):
    frase_final = ''
    for letra in frase:
        if letra not in "aeiouAEIOU":
            frase_final += letra.upper()
        
    return frase_final