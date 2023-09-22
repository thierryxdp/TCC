def retira_pontuacao(frase):
    """função que dada uma frase, retira todos os caracteres de pontuação;str-->str"""
    f=frase.replace('.',' ')
    f=f.replace(',',' ')
    f=f.replace('!',' ')
    f=f.replace('?',' ')
    f=f.replace('-',' ')
    f=f.replace(':',' ')
    f=f.replace(';',' ')
    f=f.replace('...',' ')
    return f