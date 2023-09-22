def uppCons(frase):
    """recebe uma frase e retorna essa mesma frase mas com todas as suas 
    consoantes em letra maiuscula"""
    
    i = 0
    frase_nova = ''
    consoantes = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h',
                  'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    
    while i < len(frase):
        
        if frase[i] not in consoantes:
            frase_nova += frase[i]
            
        elif frase[i] in consoantes:
            frase_nova += str.upper(frase[i])
            
        i += 1
    
    return frase_nova