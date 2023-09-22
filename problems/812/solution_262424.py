def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    str.remove(frase,'?') + str.remove(frase,'!') + str.remove(frase,'.') + str.remove(frase,'-') + str.remove(frase,',') + str.remove(frase,';')
    
    return frase