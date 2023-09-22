def retira_pontuacao(frase):
    '''teste'''
    return str.rstrip(frase,'!') and str.rstrip(frase,'.') and str.rstrip(frase,'?') and str.lstrip(frase,'-') and str.strip(frase,',')