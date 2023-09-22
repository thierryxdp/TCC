def faltante(lista):
    """determina o número faltando na lista;
    list -> int"""
    
    l_final=[]
    for contador in range(len(lista) - 1): 
        if lista[contador + 1] != lista[contador] + 1 :
            l_final.append(lista[contador] + 1)
        else:
            l_final.append(lista[-1] + 1)
    return (l_final)