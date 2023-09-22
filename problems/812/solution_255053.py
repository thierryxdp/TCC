def retira_pontuacao(frase):
    frase = frase.split()
    for i in range(len(frase)):
        for j in range(len(frase[i])):
            if frase[i][j]=="." or frase[i][j]=="!" or frase[i][j]=="?" or frase[i][j]=="-" or frase[i][j]=="," or frase[i][j]==":" or frase[i][j]==";":
                frase[i]= str.replace(frase[i],frase[i][j]," ")
    
    
    separador = ' '
    resultado = separador.join(frase)
    return resultado