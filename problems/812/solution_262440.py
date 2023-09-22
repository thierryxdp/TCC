def retira_pontuacao(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    if '-' in frase:
        return str.replace(frase,'-',' ')
    
    elif ',' in frase:
        return str.replace(frase,',',' ')
    
    elif ':' in frase:
        return str.replace(frase,':',' ')
    
    elif ';' in frase:
        return str.replace(frase,';',' ')
    
    elif '.' in frase:
        return str.replace(frase,'.',' ')
    
    elif '?' in frase:
        return str.replace(frase,'?',' ')
    
    elif '!' in frase:
        return str.replace(frase,'!',' ')
    
    elif '.' and ',' in frase:
        return str.replace(frase,'.',' ') + str.replace(frase,',',' ')