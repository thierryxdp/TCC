def retira_pontuacao(frase):
    '''Função que recebe uma frase e retorna outra frase
    onde todos os caracteres de pontuação foram substituídos
    por espaço.
    str -> str'''
    
    frase = frase.replace(";"," ")
    frase = frase.replace("-"," ")
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace("."," ")
    
    return frase