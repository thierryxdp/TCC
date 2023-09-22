def retira_pontuacao (frase):
    '''
    	essa função retira os caracteres de pontuacão e coloca no lugar um "espaço"
    '''
    return str.replace(frase,'-', ' ') and str.replace(frase,',', ' ') and str.replace(frase,'.', ' ')