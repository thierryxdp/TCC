def retira_pontuacao(frase):
    '''função que retira todas as pontuações da frase 
    '''
    frase=frase.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    return x