def contafrases(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    contagem1=frase.split('. ')
    contagem3=frase.split('?')
    contagem2=frase.split('...')
    contagem4=frase.split('!')
    if contagem1==[frase]:
        contagem1=[]
    else:
        contagem1=frase.split('. ')
    if contagem3==[frase]:
        contagem3=[]
    else:
        contagem3=frase.split('?')
    if contagem2==[frase]:
        contagem2=[]
    else:
        contagem2=frase.split('...')
    if contagem4==[frase]:
        contagem4=[]
    else:
        contagem4=frase.split('!')
    contagem=contagem1+contagem2+contagem3+contagem4
    
    return len(contagem)