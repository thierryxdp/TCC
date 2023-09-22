def inverte(frase):
    f1 = str.replace(frase, ",","").lower()
    f2 = str.replace(f1, ".","")
    f3 = str.replace(f2, "-","")

    ah = frase_limpa.split()
    inv = len(ah) - 1
    lista = []

    while inv >= 0:
        lista.append(ah[inv])
        inv -= 1
    
    inversa = " ".join(lista)
    
    return inversa