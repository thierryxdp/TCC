def retira_pontuacao(frase):
    ''' esta função substitui a pontuação de frases por espaço. str->str'''
    frase = str.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("!"," ").replace("?"," ")
    return frase