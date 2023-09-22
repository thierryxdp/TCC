def uppCons(frase):

    FM = frase.upper()

    f1 = FM.replace("A","a")
    f2 = f1.replace("E","e")
    f3 = f2.replace("I","i")
    f4 = f3.replace("O","o")
    f5 = f4.replace("U","u")
    f6 = f5.replace("Á","á")
    f7 = f6.replace("É","é")
    f8 = f7.replace("Í","í")
    f9 = f8.replace("Ó","ó")
    f0 = f9.replace("Ú","ú")
    fa = f0.replace("Ã","ã")
    fb = fa.replace("Õ","õ")
    fc = fb.replace("Ú","ú")

    return fc