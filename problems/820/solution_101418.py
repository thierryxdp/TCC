def posLetra(frase, letra , n):
    i=0
    qnt=[]
    frase=[frase]
    while  i < len(frase):           
        if frase[i] == letra:
            qnt= list.index(letra,n) 
        if n >= len(qnt):        
            return -1                    
    i=i+1
    return qnt