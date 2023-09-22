def retira_pontuacao(frase):
    '''função que retira todas as pontuações da frase 
    '''
    frase = str.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    return frase