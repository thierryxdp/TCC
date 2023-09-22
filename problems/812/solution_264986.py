def retira_pontuacao(frase):
    '''
       Dada uma frase a função retorna a mesma frase, porém 
       sem os pontos de pontuação que apresentava
       str -> str
    '''
    pontos = string.punctuation
    for x in pontos:
        retira_pontuacao = str.replace(x, '')
        return retira_pontuacao