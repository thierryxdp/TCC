def retira_pontuacao(s):
    '''Recebe uma string e retorna a mesma string sem os sinais de pontuação; string->string'''
    s2=str.replace(s,'-',' ')
    s2=str.replace(s,',',' ')
    s2=str.replace(s,':',' ')
    s2=str.replace(s,';',' ')
    s2=str.replace(s,'.',' ')
    s2=str.replace(s,'!',' ')
    s2=str.replace(s,'?',' ')
    return s2