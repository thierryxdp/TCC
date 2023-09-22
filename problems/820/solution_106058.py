def posLetra(texto, letra, f):
    i = 0 
    while i< len(texto):
        if letra in texto[i]:
            if texto[i] == texto[f]:
                pos = texto.index(texto[f])
        if letra not in texto[i]: 
            i +=1
        else: 
            pos +=1
    return pos