def filtra_pares(s):
    "tuple-->tuple"
    "filtra os elementos pares de uma tupla"
    Armazenador=()
    
   
    if ((s[0])%2==0)==True:
       "se o primeiro elemento for par ele é adicionado na tupla"
        Armazenador= Armazenador + (s[0],)
    
    if ((s[1])%2==0)==True:
       "se o segundo elemento for par ele é adicionado na tupla"
        Armazenador= Armazenador + (s[1],)

    if ((s[2])%2==0)==True:
       "se o terceiro elemento for par ele é adicionado na tupla"
        Armazenador= Armazenador + (s[2],)
    
    if ((s[3])%2==0)==True:
       "se o quarto elemento for par ele é adicionado na tupla"
        Armazenador= Armazenador + (s[3],)
   
    return Armazenador