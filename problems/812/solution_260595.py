def retira_pontuacao(s):
    '''Recebe uma string e retorna a mesma string sem os sinais de pontuação; string->string'''
    s2=str.replace(s,'-',' ')
    s3=str.replace(s2,',',' ')
    s4=str.replace(s3,':',' ')
    s5=str.replace(s4,';',' ')
    s6=str.replace(s5,'.',' ')
    s7=str.replace(s6,'!',' ')
    s8=str.replace(s7,'?',' ')
    return s8