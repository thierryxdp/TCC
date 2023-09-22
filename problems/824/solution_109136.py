uppCons(frase):
    a = 0
    while a < len(frase):
        if str.upper(frase[a]) not in (AEIOU):
            str.replace(frase,frase[a],str.upper(frase[a]))
        a += 1
    return frase