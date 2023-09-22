def retira_pontuacao(frase):
    """Funcao que recebe uma frase e retorna todos os seus caracteres de pontuacao (travessao,
virgula, dois pontos, ponto e virgula, alem da pontuacao de encerramento da frase,
sendo substituido por espaco"""
    retira = frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("!"," ").replace("."," ").replace("?"," ")
    return retira