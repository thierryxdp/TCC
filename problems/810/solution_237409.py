def inverte(frase):
    frase = frase.lower()
    frase = filtro(frase)
    lista = frase.split()
    lista.reverse()
    frase_final = ' '.join(lista)
    return frase_final