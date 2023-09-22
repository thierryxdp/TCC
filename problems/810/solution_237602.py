def retira_pontuacao(frase):
    """Esta função retorna uma outra frase onde todos os caracteres de pontuação (travessão, vírgula, dois pontos, 
    ponto e vírgula e ponto final) tenham sido substituídos por espaço."""
    a = str.replace(frase,'.',' ')
    b = str.replace(a,",",' ')
    c = str.replace(b,';',' ')
    d = str.replace(c,':',' ')
    e = str.replace(d,"-",' ')
    f = str.replace(e,'!',' ')
    g = str.replace(f,'?',' ')
    return g

def inverte(frase):
    '''Esta função retorna uma frase ao contrário, porém, sem letras maiúsculas e sem pontuação.'''
    x1 = pontuacao(frase)
    x2 = str.lower(x1)
    x3 = str.split(x2, " ")
    x4 = p3[::-1]
    x5 = str.join(" ",x4)
    return x5