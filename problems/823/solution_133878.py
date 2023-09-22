def faltante(lista):
    """determina o número faltando na lista;
    list -> int"""
    
    l_final=[]
      
    for contador in range(len(lista) - 1): 
        if lista[contador + 1] != lista[contador] + 1 :
            l_final.append(lista[contador] + 1)
    return (l_final.pop(0))
        elif lista[contador + 1] not != lista[contador] + 1:
    return (lista[-1])+1