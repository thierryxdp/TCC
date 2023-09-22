def uppCons(frase):
    frase_final = ''
    for letra in frase:
        if letra not in "aeiouAEIOUãõáóÓÁúíéú":
            frase_final += letra.upper()
        else:
            frase_final+=letra
        
    return frase_final