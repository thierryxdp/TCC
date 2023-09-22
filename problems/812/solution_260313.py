def retira_pontuacao (frase):
    '''recebe uma frase, calcula  e retorna uma frase onde os caracteres de pontuação são substituídos por espaço'''
    '''str->str'''
    return str.replace (frase,'-','')
    return str.replace (frase,',','')
    return str.replace (frase,':','')
    return str.replace (frase,';','')
    return str.replace (frase, '.','')
    return str.replace (frase, '!','')
    return str.replace (frase, '?','')