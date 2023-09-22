def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    if '-' in frase:
        str.replace(frase,'-',' ')
    
    if ',' in frase:
        str.replace(frase,',',' ')
    
    if ':' in frase:
        str.replace(frase,':',' ')
    
    if ';' in frase:
        str.replace(frase,';',' ')
        
            
    return frase + frase.replace(frase[-1],' ')