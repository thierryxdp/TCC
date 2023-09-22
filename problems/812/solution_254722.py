def retira_pontuaçao(frase):
    """Função que dada uma frase, retorna a frase em que todos os caracteres
    de pontuação(vírgula, ponto final, dois pontos, ponto e vírgula e 
    travessão) tenham sido substituídas por espaço.
    str->str
    """
    x = str.replace(frase,',',' ')
    y = str.replace(x,'.',' ')
    z = str.replace(y,':',' ')
    w = str.replace(z,';',' ')
    a = str.replace(w,'-',' ')
    return a