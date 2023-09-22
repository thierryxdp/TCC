def posLetra(frase,letra,n):
    x=list(frase)
    contador = -1
    aux = 0
    for l in x:
        contador += 1
        if letra == l:
            aux +=1
            if aux == n:
                return contador