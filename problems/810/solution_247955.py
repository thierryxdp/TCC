def retira_pontuacao(frase):
    """Recebe uma frase e devolve ela com todos os sinais(travessão, virgulo, dois pontos, ponto e virgula e os pontos de encerramento) trocados por espaços
    	str -> str"""
    str.replace(frase,'-',' ')
    str.replace(frase,',',' ')
    str.replace(frase,':',' ')
    str.replace(frase,';',' ')
    str.replace(frase,'.',' ')
    str.replace(frase,'!',' ')
    str.replace(frase,'?',' ')
    return frase

def inverte(frase):
    """Recebe uma frase e devolve ela ao contrario sem nenhum ponto;
    	str -> str"""
    retira_pontuacao(frase)
    str.split(frase,' ')
    list.reverse(frase)
    frase=str(frase)
    frase=str.strip(frase,'[')
    frase=str.strip(frase,']')
    frase=str.strip(frase,',')
    return frase