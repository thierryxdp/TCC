︎ def retira_pontuacao(x=""):
    '''função que substitui pontuações na frase por espaços'''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    return x