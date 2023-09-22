def retira_pontuacao(frase3):
    '''Função que, dada uma frase, retorna uma outra frase onde todos os
        caracteres de pontuação(travessão, vírgula, dois pontos, ponto e virgula e
        ponto final) tenham sido substituídos por espaço.
        Entrada: list(str) ; Saída: list(str)'''
    a = str.replace(frase3,'.',' ')
    b = str.replace(a,",",' ')
    c = str.replace(b,';',' ')
    d = str.replace(c,':',' ')
    e = str.replace(d,"-",' ')
    f = str.replace(e,'!',' ')
    g = str.replace(f,'?',' ')
    return g