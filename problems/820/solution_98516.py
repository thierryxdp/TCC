def posLetra(frase,letra,n_ocorrencia):
    x = frase.find(letra)
    cont = 0
    if x>=0:
        cont = cont + 1
        while (cont < n_ocorrencia):
            x = frase.find(letra,x+1)
            if x>=0:
                cont = cont + 1
            else:
                return -1
        return x
    else:
        return -1