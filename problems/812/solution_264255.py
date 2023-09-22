def retira_pontuacao(frase):
    """Função que dada uma frase retira todas suas pontuações"""
    """str->str"""
    y=frase.replace('-',' ')
    z=y.replace(',',' ')
    a=z.replace(':',' ')
    b=a.replace(';',' ')
    c=a.replace('.',' ')
    return c