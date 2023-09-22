def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    str.replace(frase,'?','') + str.replace(frase,'!','') + str.replace(frase,'.','') + str.replace(frase,'-','') + str.replace(frase,',','') + str.replace(frase,';','')
    
    return frase