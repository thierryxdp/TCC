def posLetra(frase,letra,n_ocorrencia):
    x = frase.find(letra)
    cont = 0
    if x:
        cont = cont + 1
        while (cont < n_ocorrencia):
            x = frase.find(letra,x)
            if x:
                cont = cont + 1
            else:
                return -1
    else:
        return -1