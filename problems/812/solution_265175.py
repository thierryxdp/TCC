def retira_pontuacao(x=""):
    '''função que retira todas as pontuações da frase 
    '''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    return x