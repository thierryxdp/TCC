def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos os 
    caracteres de pontuação, substituidos por espaço
    string -> string'''
    
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
    
    
    if '.' in frase:
        nova = frase.replace('.', ' ')
        return nova
    
    if '?' in frase:
        nova = frase.replace('?', ' ')
        return nova
    
    if '-' in frase:
        nova = frase.replace('-', ' ')
        return nova