def inverte (frase):
    '''retorna uma str de um frase escrita de tras pra frente sem potuacao
    da str frase
    str->str'''
    a = frase
    a = str.replace (a,'...',' ')
    a = str.replace (a,'.',' ')
    a = str.replace (a,':',' ')
    a = str.replace (a,'?',' ')
    a = str.replace (a,'!',' ')
    a = str.replace (a,'-',' ')
    a = str.replace (a,';',' ')
    a = str.strip(a)
    listaStr = str.split(a)
    listaStr = listaStr[::-1]
    b = str.join(' ',listaStr)
    return b