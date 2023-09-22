def retira_pontuacao(frase):
    """Retorna uma frase igual a de entrada, mas como a sua pontuação substituída por espaço.
    string --> string"""
    
    if '.' in frase:
        return str.replace(frase, '.', ' ')
    
    if '!' in frase:
        return str.replace(frase, '!', ' ')
    
    if '?' in frase:
        return str.replace(frase, '?', ' ')
    
    if '...' in frase:
        return str.replace(frase, '...', ' ')
    
    if '-' in frase:
        return str.replace(frase, '-', ' ')
    
    if ',' in frase:
        return str.replace(frase, ',', ' ')
    
    if ':' in frase:
        return str.replace(frase, ':', ' ')
    
    if ';' in frase:
        return str.replace(frase, ';', ' ')