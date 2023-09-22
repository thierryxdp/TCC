def retira_pontuacao(s):
    '''Recebe uma string e retorna a mesma string sem os sinais de pontuação; string->string'''
    str.replace(s,'-',' ')
    str.replace(s,',',' ')
    str.replace(s,':',' ')
    str.replace(s,';',' ')
    str.replace(s,'.',' ')
    str.replace(s,'!',' ')
    str.replace(s,'?',' ')
    return s