def filtra_pares(tupla):
    tuplaF=()
    if tupla[0]%2==0:
        tuplaF=tuplaF+(tupla[0],)
        
    if tupla[1]%2==0:
        tuplaF=tuplaF+(tupla[1],)
    
    if tupla[1]%2==0:
        tuplaF=tuplaF+(tupla[2],)
        
    if tupla[1]%2==0:
        tuplaF=tuplaF+(tupla[3],)
        
    return tuplaF