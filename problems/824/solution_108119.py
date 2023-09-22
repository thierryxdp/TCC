def uppCons (frase):
    """Função que retorna todas as consoantes em maiusculas 
    str -> str"""
    
    contador = 0
    FraseAtual = ''
    
    while contador < len(frase):
        if frase [contador] not in 'aeiou':
            FraseAtual += frase[contado].upper()
            
    return FraseAtual