def quant_palavras(frase):
    '''Retorna a quantidade de palavras da frase;
    str->int'''
    
    frase=[]
    
    if frase[0]==' ':
        frase.remove(frase)
    elif frase[1:]==' ':
        frase.remove(frase)
    else:
        return str.split(len(frase))