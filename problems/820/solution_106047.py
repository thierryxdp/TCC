def posLetra(texto, letra, f):
    i = 0 
    while True:
        if letra in texto[i]:
            if texto [i]== texto[f]:
                pos = texto.index(texto[f])
            else: 
                pos =-1
    return pos