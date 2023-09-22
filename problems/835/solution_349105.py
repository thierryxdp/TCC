def melhor_volta(m):
    """Retorna uma tupla informando:
    De quem foi a melhor volta da prova, com qual tempo e em que volta.
    list->tuple"""
    v = m[0][0]
    for i in range(len(m)):
        p = p + 1
    	for j in range(len(m[i])):
            if v < min(m[i]):
            	v = min(m[i])
    return (p,v)