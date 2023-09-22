def media_matriz(M):
    """Funcao que dada uma matriz M de inteiros nao vazia,
    retorna a media de todos os numeros da matriz com 
    exatamente duas casas decimais de precisao;
    lista->float"""
    
    S=0
    D=(len(M)*len(M[0]))
    
    for i in range(len(M)):
        for j in range(len(M[i])):
            S=S+M[i][j]
            Media=(S/D)
            
    return round(Media,2)