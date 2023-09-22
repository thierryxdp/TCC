def melhor_volta(M):
    """Uma pista de Kart permite 10 voltas para cada um dos
    6 corredores. Nesse contexto, esta funcao recebe como 
    entrada uma matriz M 6x10 com os tempos em segundos dos 
    corredores em cada volta. A funcao retorna uma tupla
    informando: De quem foi a melhor volta, com qual tempo 
    e em que volta. Assume-se que os corredores tem tempos
    diferente;
    lista->tupla"""
    
    L=[]
    
    for i in range(len(M)):
        for j in range(len(M[i])):
            L=L+M[i][j]
            
    Menortempo=min(L)
    
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]=Menortempo:
                Corredor=i+1
                Volta=j+1
                
    return (Corredor,Menortempo,Volta)