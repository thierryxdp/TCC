def uppCons(frase):
    """recebe uma frase e retorna essa mesma frase mas com todas as suas 
    consoantes em letra maiuscula"""
    
    i = 0
    frase_nova = ''
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    while i < len(frase):
        
        if frase[i] in vogais:
            frase_nova += frase[i]
            
        elif frase[i] != vogais:
            frase_nova += str.upper(frase[i])
            
        i += 1
    
    return frase_nova