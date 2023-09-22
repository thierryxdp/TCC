def retira_pontuacao(frase):
    ''' Funcao que, dada uma frase, substitui todos os caracteres de pontuação e substitui por espaço
         string -> string'''
    import re
    return re.sub(r',|.|:|?|!|;', " ", frase)