def inverte(frase):
    """Função que escreve a uma frase na ordem iversa;str->str """
    frase = frase.split()
    for i in range(len(frase)):
        for j in range(len(frase[i])):
            if frase[i][j]=="." or frase[i][j]=="!" or frase[i][j]=="?" or frase[i][j]=="-" or frase[i][j]=="," or frase[i][j]==":" or frase[i][j]==";":
                frase[i]= str.replace(frase[i],frase[i][j]," ")
    

    separador = ' '
    resultado = separador.join(frase)
    resultado = str.lower(resultado)

    frase3= str.split(resultado)[::-1]
    frase4= separador.join(frase3)
    return frase4