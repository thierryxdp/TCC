def posLetra(palavra,letra,n):
    ''' Entrada -> string, string, int
        Saída -> int'''
    
    Q = len(palavra) #quantidade de caracteres
    p = str.index(palavra,letra)
    c = str.count(palavra,letra)
    i = 0 #contador e indice
    acu = 0 #acumulador 
    
    #Quando o indice inserido corresponde a 1ª ocorrência
    if n == p:
        return p
    
    #Quando existem menos ocorrência do que o usuário indica em (n)
    elif c < n:
        return -1
    
    while i <= Q-1:
        if acu == n:
            return i-1
        
        elif palavra[i] == letra:
            acu = acu + 1
        i = i + 1