def retira_pontuacao(frase):
    """A função recebe uma frase, e retorna uma frase em que os caracteres
    de pontuação, sendo: travessão, vírgula, dois pontos, ponto e 
    vírgula e pontuação de encerramento da frase são substituidos 
    por espaço;
    str -> str"""
    frase = frase.replace("-"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace(";"," ")
    frase = frase.replace("."," ")
    frase = frase.replace("?"," ")
    frase = frase.replace("!"," ")
    return frase