def conta_frases(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    frasetrue=str.replace(frase,'...','.')
    contagem1=frase.split('.')
    contagem3=frase.split('?')
    contagem4=frase.split('!')
    
    
    if contagem1==[frase]:
        contagem1=0
    else:
        contagem1=len(frasetrue.split('.'))
        
        
        
    if contagem3==[frase]:
        contagem3=0
    else:
        contagem3=len(frasetrue.split('?'))-1
        
        
        
    if contagem4==[frase]:
        contagem4=0
    else:
        contagem4=len(frasetrue.split('!'))-1

    
    return contagem1+contagem3+contagem4
        
        
        
    if contagem3==[frase]:
        contagem3=[]
    else:
        contagem3=frasetrue.split('?')
        
        
        
    if contagem4==[frase]:
        contagem4=[]
    else:
        contagem4=frasetrue.split('!')
    contagem=contagem1+contagem3+contagem4
    
    return len(contagem)