def retira_pontuacao (frase):
    '''recebe uma frase, calcula  e retorna uma frase onde os caracteres de pontuação são substituídos por espaço'''
    '''str->str'''
    um = str.index (str.replace (frase,'-',''))
    dois =  str.replace (frase,',','')
    tres = str.replace (frase,':','')
    quatro = str.replace (frase,';','')
    quinto = str.replace (frase, '.','')
    sexto = str.replace (frase, '!','')
    setimo = str.replace (frase, '?','')
    return