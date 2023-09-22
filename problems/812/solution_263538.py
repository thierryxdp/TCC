def retira_pontuacao (frase):
    '''retorna uma str com as pontuacoes substituidas por espaço da str frase
    str->str'''
    a = frase
    a = str.replace(a,'-',' ')
    a = str.replace(a,',',' ')
    a = str.replace(a,'...',' ')
    a = str.replace(a,':',' ')
    a = str.replace(a,'.',' ')
    a = str.replace(a,';',' ')
    a = str.replace(a,'!',' ')
    a = str.replace(a,'?',' ')
    return a