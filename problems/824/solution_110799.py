def uppCons(frase):
    """ Dada uma frase de entrada, retorne a mesma frase
        com todas as letras maiúsculas
        str->str"""
    i = 0
    novafrase =''
    
    while i < len(frase):
        if frase[i] in "bcçdfghklmnpqrstvwxz":
            novafrase += str.upper(frase[i])
        else:
            novafrase += frase[i]
            i += 1
    return novafrase