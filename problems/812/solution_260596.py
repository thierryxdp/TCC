def retira_pontuacao (frase:str) -> str:
    '''Substitui toos os caracteres de pontuação (p)
    da frase de entrada(frase) por espaço, retornando
    uma frase com alterações (fa) com as substituições.'''
    
    p = ['.', '!', '?', '-', ',', ';', ':', '...']
    
    fa = frase

    fa = fa.replace(',', ' ')
    fa = fa.replace(';', ' ')
    fa = fa.replace(':', ' ')
    fa = fa.replace('...', ' ')
    fa = fa.replace('.', ' ')
    fa = fa.replace('!', ' ')
    fa = fa.replace('?', ' ')
    fa = fa.replace('-', ' ')
   
    
    return fa