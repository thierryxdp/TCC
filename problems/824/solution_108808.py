def uppCons(frase):
    """Dada uma frase, retorna a frase original com apenas as consoantes em maiuscula"""
    """entrada: str
    saida: str"""
    
    frase1 = ''
    pos = 0
    
    while pos < len(frase):
        if frase[pos] in 'qwrtyplkjhgfdszxcvbnmç':
            maiuscula = str.upper(frase[pos])
            frase1 = frase1 + maiuscula
            pos = pos +1
        
        elif frase[pos] not in 'qwrtyplkjhgfdszxcvbnmç':
            frase1 = frase1 + frase[pos]
            pos = pos +1
            
    return frase1