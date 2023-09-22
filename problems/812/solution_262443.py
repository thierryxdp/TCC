def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    if '-' in frase:
        frase1 = str.replace(frase,'-',' ')
    
    if ',' in frase:
        frase1 = str.replace(frase,',',' ')
    
    if ':' in frase:
        frase1 = str.replace(frase,':',' ')
    
    if ';' in frase:
        frase1 = str.replace(frase,';',' ')
        
            
    return frase1 + frase.pop()