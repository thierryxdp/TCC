def retira_pontuacao(frase):
    ''' esta função substitui a pontuação de frases por espaço. str->str'''
    return frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("!"," ").replace("?"," ")