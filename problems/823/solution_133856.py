def faltante(lista):
    """determina o número faltando na lista;
    list -> int"""
    
    lista_final = []    
    
    for contador in range(len(lista) - 1): 
        if lista[contador + 1] != lista[contador] + 1 :
            lista.append(lista[contador] + 1)
            
    return lista_final