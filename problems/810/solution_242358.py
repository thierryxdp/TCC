def inverte(s):
    '''Recebe uma string e retorna a mesma string sem os sinais de pontuação, em caixa baixa e invertida; string->string'''
    s2=str.replace(s,'-',' ')
    s3=str.replace(s2,',',' ')
    s4=str.replace(s3,':',' ')
    s5=str.replace(s4,';',' ')
    s6=str.replace(s5,'.',' ')
    s7=str.replace(s6,'!',' ')
    s8=str.replace(s7,'?',' ')
    s9=str.lower(s8)
    s10=str.split(s9)
    s11=str.join(s9[::-1],' ')
    return s11