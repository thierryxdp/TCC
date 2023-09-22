def filtra_pares(s):
    "filtra os elementos pares de uma tupla"
    Armazenador=()
    
   
    if ((s[0])%2==0)==True and ((s[1])%2==0)==True and ((s[2])%2==0)==True and ((s[3])%2==0)==True:
        return Armazenador + (s[0],) + (s[1],) + (s[2],) + (s[3],)
     
    
    if ((s[0])%2==0)==False and ((s[1])%2==0)==True and ((s[2])%2==0)==True and ((s[3])%2==0)==True:
        return Armazenador + (s[1],) + (s2],) + (s[3],)
    
    if ((s[0])%2!=0) and ((s[1])%2!=0) and ((s[2])%2!=0) and ((s[3])%2!=0):
        return Armazenador