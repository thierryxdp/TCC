def uppCons(frase):
    i = 0
    frase1 = []
    while i < len(frase):
        if str.lower(frase[i]) in "bcdfghjklmnpqrstvxywzç":
            list.append(frase1, str.upper(frase[i]))
        else:
            list.append(frase1, frase[i])
        i = i + 1
    return str.join("", frase1)