def retira_pontuacao(frase):
    ''' troca as pontuações por um eswpaço vazio'''
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    return frase