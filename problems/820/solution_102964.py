def posLetra(frase,letra,num):
    contador = 0
    i=0
    while i < len(frase):
        if frase[i] in letra:
           contador += 1
        i+=1
    if contador < num:
        contador = -1
        return contador
    return contador