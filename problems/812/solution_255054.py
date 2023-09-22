def retira_pontuacao(frase):
"""Função que retira as pontuações de uma frase;str->str"""
    frase = frase.split()
    for i in range(len(frase)):
        for j in range(len(frase[i])):
            if frase[i][j]=="." or frase[i][j]=="!" or frase[i][j]=="?" or frase[i][j]=="-" or frase[i][j]=="," or frase[i][j]==":" or frase[i][j]==";":
                frase[i]= str.replace(frase[i],frase[i][j]," ")
    
    
    separador = ' '
    resultado = separador.join(frase)
    return resultado