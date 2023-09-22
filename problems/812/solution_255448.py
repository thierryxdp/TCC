def retira_pontuacao(frase):
    '''uma função que substitui todos os caracteres de pontuação de uma frase por espaço'''
    nfrase  = str.replace(frase,("!","?",".","_","-",","";"":")," ")
    return nfrase