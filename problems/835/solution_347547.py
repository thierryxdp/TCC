def melhor_volta(matriz):
    """Função que, dada uma matriz 6x10, retorna uma tupla falando quem foi a melhor volta
    da prova, com qual tempo e em que volta.
    Entrada: lista
    Saída: tupla."""
    
    melhor = []
    volta = []
    
    for i in matriz:
        melhor += [min(i)]
        volta += [list.index(i,min(i))]
        
    melhor_piloto = list.index(melhor,min(melhor)+1
    #melhor_volta = min(melhor)
    #n_volta = volta[list.index(melhor,min(melhor)]+1
        
    return ((melhor_piloto))