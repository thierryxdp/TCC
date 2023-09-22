def retira_pont(frase):
    '''Função que troca todas as pontuações por espaço;
    str -> str'''
        
    return  str.remove(frase,'?') + str.remove(frase,'!') + str.remove(frase,'.') + str.remove(frase,'-') + str.remove(frase,',') + str.remove(frase,';')