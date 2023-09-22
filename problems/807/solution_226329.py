def conta_frases(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    contagem1=frase.split('.')
    contagem3=(frase.split('?'))
    contagem4=(frase.split('!'))
    
    
    if contagem1==[frase]:
        contagem1=[]
    else:
        contagem1=(frase.split('.'))
    
        
        
    if contagem3==[frase]:
        contagem3=[]
    else:
        contagem3=(frase.split('?'))

        
        
    if contagem4==[frase]:
        contagem4=[]
    else:
        contagem4=(frase.split('!'))
    if (len(frase.split('.')))>=3:
        return int(len(contagem3+contagem4+contagem1)-len(frase.split('.'))+2*len((frase.split('.')))/4)
    else:
        return int(len(contagem3+contagem4+contagem1))