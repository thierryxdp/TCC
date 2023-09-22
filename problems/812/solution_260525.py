def retira_pontuacao (frase):
    '''
    	essa função retira os caracteres de pontuacão e coloca no lugar um "espaço"
    '''
    frase = frase.replace('-', ' ') and frase.replace('.', ' ') and frase.replace(',', ' ')
    return frase