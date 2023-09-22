def melhor_volta(m):
    """função que recebe uma matriz de 6x10 com o tempo em segundos de 6 corredores e retorna uma tupla informando de quem foi a melhor volta e com qual tempo e em qual volta
	list -> tuple"""
    
    volta = []
    
    for corredor_kart in m:
        list.append(volta,min(corredor_kart))
    
    a = min(volta)
    b = list.index(volta, a)
    c = list.index(m[b],a)
    
    return (b, a, c)