def retira_pontuacao(frase):
    """funcao que indicada uma frase retorna a frase sem pontuacao;
    str->str"""
    fa=str.replace(frase,','," ")
    fb=str.replace(fa,'-'," ")
    fc=str.replace(fb,':'," ")
    fd=str.replace(fc,';'," ")
    fe=str.replace(fd,'.'," ")
    fg=str.replace(fe,'?'," ")
    fx=str.replace(fg,'!'," ")
    return fh