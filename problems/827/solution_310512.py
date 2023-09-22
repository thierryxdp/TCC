def qtd_divisores(nmr):
    contador = 0 
    for elemento in range (1, nmr):
        if nmr % elemento == 0:
            contador += 1
    if nmr <= 0:
        return contador
    else:
        return contador + 1