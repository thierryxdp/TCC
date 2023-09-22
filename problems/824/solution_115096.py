def uppCons(frase):
    '''dado uma frase, retorna a frase com todas as suas consoantes em maiusculo, e as demais 
do jeito que estava. 
str -> str'''

    i = 0
    frase2 = []
    while i < len(frase):
        if str.lower(frase[i]) in "bcdfghjklmnpqrstvxywzç":
            list.append(frase2, str.upper(frase[i]))
        else:
            list.append(frase2, frase[i])
        i = i + 1
    return str.join("", frase2)