def retira_pont(frase):
    '''Função que troca todas as pontuações por espaço;
    str -> str'''
    
       frase = str.remove(frase,'.')
    frase = str.remove(frase,'!')
    frase = str.remove(frase,'?')
    
    return  str.remove(frase,'-') + str.remove(frase,',') + str.remove(frase,';')