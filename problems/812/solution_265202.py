def retira_pontuacao(x=""):
    '''
    funcao que retira as pontucoes da frase
    
    '''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("!"," ") 
    return x