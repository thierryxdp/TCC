def lingua_p(palavra):
    """Função que, dada uma palavra, retorna essa mesma palavra traduzida para a língua do P; string->string"""
    
    minuscula = str.lower(palavra)
    trad = ''
    
    for x in palavra:
        
        if x in 'aeiouáâãéêóô':
            
            trad = trad + x + 'p' + x
            
        elif x in 'bcdfghjklmnpqrstvwxyzç':
            
            trad = trad + x
            
    return trad