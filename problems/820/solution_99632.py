def posLetra(frase,l,n):
    """recebe uma frase e informa a n ocorrencia da de l na 
    frase:str,str,int->int"""
    i=0
    while i<(n):
        if l in frase:
            str.replace(frase,l,'',1)
    i=i+1
        else:
            return -1
    return str.find(frase,l)