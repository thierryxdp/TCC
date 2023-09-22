def retira_pontuacao(frase):
    '''função que retira todas as pontuações da frase 
    '''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    return x