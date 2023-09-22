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
    
    and if '.' in frase:
        return str.replace(frase,'.',' ')
    
    and if '?' in frase:
        return str.replace(frase,'?',' ')
    
    and if '!' in frase:
        return str.replace(frase,'!',' ')