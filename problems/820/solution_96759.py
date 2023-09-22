def posLetra(palavra,letra,n):
    '''A função retornará qual o indice da (n)ézima ocorrência da (letra) na (palavra)
    Dados de entrada -> string, string, int
    Dados de saída -> int'''
    
    i = 0 #contador e indice
    Q = len(palavra) #quantidade de caracteres
    p = str.index(palavra,letra) # indice da primeira ocorrência
    
    if n == p:
        return p
    
    while i <= Q-1:
        if