def retira_pontuacao(frase):
    '''...'''
    palavra = str.replace(frase,'?',' ') + str.replace(frase,'.',' ')
    
    return palavra