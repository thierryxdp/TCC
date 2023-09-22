def retira_pontuacao(frase):
    '''dada uma frase, retorna a mesma substituindo as pontuações por 
    espaço.
    str -> str'''
    
    return frase.replace("!"," ").replace("?"," ").replace("."," ").replace(";"," ").replace("-"," ")