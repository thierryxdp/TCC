def melhor_volta(matriz):
    """Função que, dada uma matriz 6x10, retorna uma tupla falando quem foi a melhor volta
    da prova, com qual tempo e em que volta.
    Entrada: lista
    Saída: tupla."""
    
    melhor = []
    volta = []
    
    for i in matriz:
        melhor += max(i)
        volta += list.index(i,max(i))
        
    return (((list.index(melhor, max(melhor))), max(melhor), (volta[list.index(melhor, max(maior))]))