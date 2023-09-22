def retira_pontuacao(x=""):
    '''função que substitui pontuações na frase por espaços'''
    return x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")