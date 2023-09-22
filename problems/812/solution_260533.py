def retira_pontuacao (frase):
    '''
    	essa função retira os caracteres de pontuacão e coloca no lugar um "espaço"
    '''
    for x in "?!-:;,.":
        frase = frase.replace(x, "")
    return frase