def uppCons(frase):
    '''dada uma frase, retorna a frase com todas as suas consoantes
    em maiusculas (e os demais caracteres exatamente como estavam
    str->str'''

    i = 0
    frase2 = []
    while i < len(frase):
        if str.lower(frase[i]) in "bcçdfghjklmnpqrstvxywz":
            list.append(frase2, str.upper(frase[i]))
        else:
            list.append(frase2, frase[i])
        i = i + 1
    return str.join("", frase2)