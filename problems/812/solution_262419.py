def retira_pont(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    frase = str.remove(frase,'?') + str.remove(frase,'!') + str.remove(frase,'.') + str.remove(frase,'-') + str.remove(frase,',') + str.remove(frase,';')
    
        
    return  frase