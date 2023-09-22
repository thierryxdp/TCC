def retira_pontuacao (frase):
    '''recebe uma frase, calcula  e retorna uma frase onde os caracteres de pontuação são substituídos por espaço'''
    '''str->str'''
    um =  str.replace (frase,'-','',(str.index(frase, '-'))
    dois =  str.replace (frase,',',''(str.index(frase, ','))
    tres = str.replace (frase,':','')
    quatro = str.replace (frase,';','')
    quinto = str.replace (frase, '.','')
    sexto = str.replace (frase, '!','')
    setimo = str.replace (frase, '?','')
    return um + dois + tres + quatro + quinto + sexto + setimo