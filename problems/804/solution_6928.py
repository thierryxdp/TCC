def filtra_pares(s):
    "filtra os elementos pares de uma tupla"
    Armazenador=()
    
   
    if ((s[0])%2==0)==True:
        return (s[0],)
    Armazenador1= Armazenador1 + (s[0],)
    
    if ((s[1])%2==0)==True:
        return(s[1],)
    Armazenador2= Armazenador2 + (s[1],)

    if ((s[2])%2==0)==True:
        return (s[2],)
    Armazenador3= Armazenador3 + (s[2],)
    
    if ((s[3])%2==0)==True:
        return(s[3],)
    Armazenador4= Armazenador4 + (s[3],)
   
    return Armazenador1 + Armazenador2 + Armazenador3 + Armazenador4