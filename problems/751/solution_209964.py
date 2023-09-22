def quant_palavras(frase):
    '''Retorna a quantidade de palavras da frase;
    str->int'''
    
    frase=[]
    
    if frase[0]==' ':
        frase.remove(frase,0)
    elif frase[1:]==' ':
        frase.remove(frase,[1:])
    else:
        return str.split(len(frase))