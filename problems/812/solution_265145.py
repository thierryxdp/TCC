def retira_pontuacao(x=""):
    '''
    função que retira toda a pontuação de 
    uma frase
    
    '''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    return x