def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    if ('?' or '!' or '.' or ';' or ',' or '-' ) in frase:
        str.replace(frase,';',' ') + str.replace(frase,'?',' ') + str.replace(frase,'-',' ') + str.replace(frase,'!',' ') + str.replace(frase,'.',' ')