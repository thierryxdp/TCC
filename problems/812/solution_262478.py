def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    if '-' in frase:
        frase = str.replace(frase,'-',' ') and str.replace(frase[-1],' ')
    
    if ',' in frase:
        frase = str.replace(frase,',',' ') and str.replace(frase[-1],' ')
    
    if ':' in frase:
        frase = str.replace(frase,':',' ') and str.replace(frase[-1],' ')
    
    if ';' in frase:
        frase = str.replace(frase,';',' ') and str.replace(frase[-1],' ')
        
    
            
    return frase