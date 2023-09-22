def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna uma outra frase onde todos os
        caracteres de pontuação(travessão, vírgula, dois pontos, ponto e virgula e
        ponto final) tenham sido substituídos por espaço.
        str -> str"""
    a = str.replace(frase,'.',' ')
    b = str.replace(a,",",' ')
    c = str.replace(b,';',' ')
    d = str.replace(c,':',' ')
    e = str.replace(d,"-",' ')
    f = str.replace(e,'!',' ')
    g = str.replace(f,'?',' ')
    return g