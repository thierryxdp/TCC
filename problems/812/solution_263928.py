def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos os 
    caracteres de pontuação, substituidos por espaço
    string -> string'''
    nova = frase.replace('.',' ')
    
    if '/' in frase:
        nova = frase.replace('/', ' ')
        return nova
    
    if '!' in frase:
        nova = frase.replace('!', ' ')
        return nova
    
    if ',' in frase:
        nova = frase.replace(',', ' ')
        return nova
    
    if ':' in frase:
        nova = frase.replace(':', ' ')
        return nova
    
    if ';' in frase:
        nova = frase.replace(';', ' ')
        return nova
    
    
    if '.' and ',' in frase:
        nova = frase.replace('.', ' ')
        return nova
        
       
    
    if '?' in frase:
        nova = frase.replace('?', ' ')
        return nova
    
    if '-' in frase:
        nova = frase.replace('-', ' ')
        return nova