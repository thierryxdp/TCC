def retira_pontuacao(frase):
    """Recebe uma frase e devolve ela com todos os sinais(travessão, virgulo, dois pontos, ponto e virgula e os pontos de encerramento) trocados por espaços
    	str -> str"""
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    return frase

def inverte(frase):
    retira_pontuacao(frase)
    str.split(frase,' ')
    list.reverse(frase)
    str(frase).strip([])
    return frase