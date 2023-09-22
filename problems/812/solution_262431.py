def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    if '?' in frase:
        return  str.replace(frase,'?',' ')
    
    if '!' in frase:
        return str.replace(frase,'!',' ')
    
    if '.' in frase:
        return str.replace(frase,'.',' ')
    
    if '-' in frase:
        return str.replace(frase,'-',' ')
    
    if ',' in frase:
        return = str.replace(frase,',',' ')
    
    if ';' in frase:
        return str.replace(frase,';',' ')