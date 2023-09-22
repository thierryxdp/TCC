def inverte(frase):
    frase = frase.split()
    for i in range(len(frase)):
        for j in range(len(frase[i])):
            if frase[i][j]=="." or frase[i][j]=="!" or frase[i][j]=="?" or frase[i][j]=="-" or frase[i][j]=="," or frase[i][j]==":" or frase[i][j]==";":
                frase[i]= str.replace(frase[i],frase[i][j]," ")
        
    frase2 = []
    for i in (range(1+len(frase))):
        frase2.append(frase[-i])

    del(frase2[0])
    separador = ' '
    resultado = [separador.join(frase2)]
    return resultado