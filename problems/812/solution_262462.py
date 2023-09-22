def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    if '-' in frase:
        msg = str.replace(frase,'-',' ')
    
    if ',' in frase:
        msg = str.replace(frase,',',' ')
    
    if ':' in frase:
        msg = str.replace(frase,':',' ')
    
    if ';' in frase:
        msg = str.replace(frase,';',' ')
        
            
    return msg + frase.replace(frase[-1],' ')