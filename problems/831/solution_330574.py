def lingua_p(palavra):
    """..."""
    
    mini = str.lower(palavra)
    traducao = ''
    
    for x in palavra:
        
        if x in 'aeiouáâãéêóôú':
            
            traducao = traducao + x + 'p' + x
            
        elif x in 'bcdfghjklmnpqrstvwxyzç':
            
            traducao = traducao + x
            
    return traducao