def conta_frases(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    contagem1=len(frase.split('.'))
    contagem3=len(frase.split('?'))
    contagem4=len(frase.split('!'))
    
    
    if contagem1==[frase]:
        contagem1=[]
    else:
        contagem1=len(frase.split('.'))-4*(str.count(frase,'...'))
    
        
        
    if contagem3==[frase]:
        contagem3=[]
    else:
        contagem3=len(frase.split('?'))
        
        
        
    if contagem4==[frase]:
        contagem4=[]
    else:
        contagem4=len(frase.split('!'))
    contagem=contagem1+contagem3+contagem4
    
    return (contagem)