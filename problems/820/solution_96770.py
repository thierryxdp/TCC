def posLetra(palavra,letra,n):
    '''A função retornará qual o indice da (n)ézima ocorrência da (letra) na (palavra)
    Dados de entrada -> string, string, int
    Dados de saída -> int'''   
    
    Q = len(palavra) #quantidade de caracteres
    p = str.index(palavra,letra) # indice da primeira ocorrência
    c = str.count(palavra,letra) #contando a quantidade de ocorrência
    i = 0 #contador e indice
    acumulado = 0
    
    #Quando o indice inserido corresponde a primeira ocorrência
    if n == p:
        return p
    
    #Quando existem menos ocorrência do que o usuário indica em (n)
    elif c < n:
        return -1
    
    while i <= Q-1:
        if palavra[i] == letra:
            return i
        i = i + 1