def inverte(frase):
    frase_limpa = str.replace(frase, ",","").lower()

    ah = frase_limpa.split()
    inv = len(ah) - 1
    lista = []

    while inv >= 0:
        lista.append(ah[inv])
        inv -= 1
    
    inversa = " ".join(lista)
    
    return inversa