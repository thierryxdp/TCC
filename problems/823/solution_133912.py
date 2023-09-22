def faltante(lista):
    """determina o número faltando na lista;
    list -> int"""
    
    listacopia= lista
    l_final = []
    for contador in range(len(listacopia) - 1): 
        if listacopia[contador + 1] != listacopia[contador] + 1 :
            l_final.append(lista[contador] + 1)
            return (l_final[0]) else (lista[-1])+1