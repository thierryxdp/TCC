def freq_palavras(frases):
    """
    recebe uma string e retorna um dicionário onde cada palavra
    da string seja uma chave e o seu valor seja seu número de
    aparições.
    """
    lista=str.split(frases,' ')
    
    dicio={}
    
    for x in lista:
        if x in dicio:
            dicio[x]+=1
        if x not in dicio:
            dicio[x]=1
            
    return dicio