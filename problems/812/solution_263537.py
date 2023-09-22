def retira_pontuacao (frase):
    '''retorna uma str com as pontuacoes substituidas por espaço da str frase
    str->str'''
    a = str.replace(frase,'-',' ')
    a = str.replace(frase,',',' ')
    a = str.replace(frase,'...',' ')
    a = str.replace(frase,':',' ')
    a = str.replace(frase,'.',' ')
    a = str.replace(frase,';',' ')
    a = str.replace(frase,'!',' ')
    a = str.replace(frase,'?',' ')
    return a