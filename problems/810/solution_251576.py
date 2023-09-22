#de tras pra frente:

def inverte(frase):

    f1 = str.replace(frase, ",","").lower()

    f2 = str.replace(f1, ".","")

    f3 = str.replace(f2, "-"," ")

    f4 = str.replace(f3, "?"," ")

    f5 = str.replace(f4, "!"," ")

    ah = f5.split()

    inv = len(ah) - 1

    lista = []

    while inv >= 0:

        lista.append(ah[inv])

        inv -= 1

    

    inversa = " ".join(lista)

    

    return inversa