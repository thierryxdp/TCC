def fatorial(N):
    """
    
    """
    lista_AntecessoresN = list(range(1,N+1))
    N_fatorial=1
    i=0
    
    while i<len(lista_numeroAntecessores):
        if lista_numeroAntecessores[i]>0:
            N_fatorial=Nfatorial*lista_numeroAntecessores[i]
        i=i+1  
    return N_fatorial