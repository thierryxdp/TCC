def retira_pontuacao(frase):
    """Função que, dada uma frase, substitui todos os
    caracteres de pontuação por espaços"""
    a = str.replace(frase,'?',' ')
    b = str.replace(a,'!',' ')
    c = str.replace(b,'...',' ')
    d = str.replace(c,'.',' ')
    e = str.replace(d,'-',' ')
    f = str.replace(e,',',' ')
    g = str.replace(f,':',' ')
    h = str.replace(f,';',' ')
    return h