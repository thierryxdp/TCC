def colchao(medidas,H,L):
    
    medidas = [A:str,B:str,C:str]
    meio = medidas.sort()
    meio1 = meio[1]
    if min(medidas) > min(H,L):
        return False
    elif meio1 > max(H,L):
        return False
    else:
        return True