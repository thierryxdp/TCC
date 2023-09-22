def conta_frases(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    contagem1=len(frase.split('.'))
    contagem3=len(frase.split('?'))
    contagem4=len(frase.split('!'))
    
    
    if contagem1==[frase]:
        contagem1=len([])
    else:
        contagem1=len(frase.split('.'))
    
        
        
    if contagem3==[frase]:
        contagem3=len([])
    else:
        contagem3=len(frase.split('?'))

        
        
    if contagem4==[frase]:
        contagem4=len([])
    else:
        contagem4=len(frase.split('!'))
    return (contagem1)-len(frase.split('.'))+2