def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    if '-' in frase:
        frase = str.replace(frase,'-',' ') and frase[-1].replace(' ')
    
    if ',' in frase:
        frase = str.replace(frase,',',' ') and frase[-1].replace(frase[-1],' ')
    
    if ':' in frase:
        frase = str.replace(frase,':',' ') and frase[-1].replace(frase[-1],' ')
    
    if ';' in frase:
        frase = str.replace(frase,';',' ') and frase[-1].replace(frase[-1],' ')
        
    frase[-1].del
            
    return frase