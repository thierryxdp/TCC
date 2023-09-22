def retira_pontuacao(frase):
    """Função que, dada uma frase, retorne a frase onde todos os caracteres
    de pontuação, incluindo travessão, vírgula, dois pontos, ponto e vírgula,
    além da pontuação de encerramento de frase, tenham sido substituídos
    por espaço.
    str -> str
    """

    x = str.replace(frase,'...',' ')
    y = str.replace(x,',',' ')
    z = str.replace(y,'-',' ')
    w = str.replace(z,':',' ')
    a = str.replace(w,'?',' ')
    b = str.replace(a,'!',' ')
    c = str.replace(b,'.',' ')
    d = str.replace(c,';',' ')
    return d