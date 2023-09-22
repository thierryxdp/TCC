def posLetra(frase,l,n):
    """recebe uma frase e informa a n ocorrencia da de l na 
    frase:str,str,int->int"""
    i=0
    a=frase
    while i<(n):
        if l in frase:
            str.replace(a,l,'',1)
        i=i+1
    if l not in frase:
        return -1
        
    return str.find(a,l)