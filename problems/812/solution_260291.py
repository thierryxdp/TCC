def retira_pontuacao (frase):
    '''recebe uma frase, calcula  e retorna uma frase onde os caracteres de pontuação são substituídos por espaço'''
    '''str->str'''
    travessao = str.replace (frase, '-','')
    virgula = str.replace (frase, ',','')
    dois pontos = str.replace (frase, ':','')
    ponto e virgula = str.replace (frase, ';','')
    ponto final = str.replace (frase, '.','')
    exclamacao = str.replace (frase, '!','')
    interrogacao = str.replace (frase, '?','')
    teste = travessao + virgula + dois pontos + ponto virgula + ponto final + exclamacao + interrogacao
    return teste