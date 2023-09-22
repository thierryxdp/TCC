def uppCons(frase):
    vow = ["a", "e", "i", "o", "u"]
    frase2 = []
    for i in frase:
        if i.lower() not in vow:
            frase2.append(i)

    return "".join(frase2)