def filtra_pares(tup):
    """Dado como entrada a trupla com quatro elementos inteiros, retorna
    uma trupla com apenas os elementos pares;
    trupla(int,int,int,int)->trupla"""
    num_pares=()
    if tup[0]%2 == 0:
        num_pares+=(tup[0],)
    if tup[1]%2 == 0:
        num_pares+=(tup[1],)
    if tup[2]%2 == 0:
        num_pares+=(tup[2],)
    if tup[3]%2 == 0:
        num_pares+=(tup[3],)
    return num_pares