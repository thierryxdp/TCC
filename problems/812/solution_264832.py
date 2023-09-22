def retira_pontuacao (frase):
    '''função que recebe uma frase e retorna a mesma frase sem pontuação
        str -> str'''
    frase = frase.replace("."," ")
    frase = frase.replace("/"," ")
    frase = frase.replace(";"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace("-"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace("!"," ")
    
    return frase