def posLetra(frase,letra,n):
    i=0
    qnt=0
    
    while i<len(frase):
        if frase[i]==letra:
             qnt= qnt + str.index(frase,letra,n)
        elif n < len(qnt):
            return -1
           
        i=i+1    
    return qnt