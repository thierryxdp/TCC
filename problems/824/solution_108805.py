def uppCons(frase):
    """Dada uma frase, retorna a frase original com apenas as consoantes em maiuscula"""
    """entrada: str
    saida: str"""
    
    frase1 = ''
    pos = 0
    
    while pos < len(frase):
        if frase[pos] in 'qwrtyplkjhgfdszxcvbnm':
            str.join(str.upper(frase[pos]),frase1)
        	pos = pos +1
        
        elif frase[pos] not in 'qwrtyplkjhgfdszxcvbnm':
            str.join(frase[pos],frase1)
            pos = pos +1
            
    return frase1