def retira_pontuacao (frase):
    '''
       Dada uma frase retorna a mesma frase sem os caracteres
       de pontuação que apresentava a frase de entrada
       str -> str
    '''
    pontos = ('.','!','?','...','-',',',':',';')
    frase = str.replace(frase,pontos,'')
    return frase