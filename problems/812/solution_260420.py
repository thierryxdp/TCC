def retira_pontuacao(texto):
    '''função que a partir de um texto em formato string retorna esse mesmo texto(tambem em formato string) em que todos os tipos de pontuação especificados foram subistituidos por espaço;string->string'''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,'-',' '),',',' '),':',' '),'.',' '),'?',' '),'!',' ')