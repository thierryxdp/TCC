def retira_pontuacao(x=""):
    '''função que substitui pontuações na frase por
    espaços
    str>>str'''
    return x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")