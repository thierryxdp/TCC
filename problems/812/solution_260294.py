def retira_pontuacao (frase):
    '''recebe uma frase, calcula  e retorna uma frase onde os caracteres de pontuação são substituídos por espaço'''
    '''str->str'''
    travessao = str.replace (frase, '-','')
    virgula = str.replace (frase, ',','')
    dois_pontos = str.replace (frase, ':','')
    ponto_e_virgula = str.replace (frase, ';','')
    ponto_final = str.replace (frase, '.','')
    exclamacao = str.replace (frase, '!','')
    interrogacao = str.replace (frase, '?','')
    teste = travessao + virgula + dois_pontos + ponto_e_virgula + ponto_final + exclamacao + interrogacao
    return teste