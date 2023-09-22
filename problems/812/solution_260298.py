def retira_pontuacao (frase):
    '''recebe uma frase, calcula  e retorna uma frase onde os caracteres de pontuação são substituídos por espaço'''
    '''str->str'''
    travessao = frase.replace ('-','','')
    virgula = frase.replace (',','')
    dois_pontos = frase.replace (':','')
    ponto_e_virgula = frase.replace (';','')
    ponto_final = str.replace (frase, '.','')
    exclamacao = str.replace (frase, '!','')
    interrogacao = str.replace (frase, '?','')
    teste = travessao + virgula + dois_pontos + ponto_e_virgula + ponto_final + exclamacao + interrogacao
    return teste