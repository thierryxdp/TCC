def quebra_cabeca(lista):
    """determina o número faltando na lista;
    list -> int"""
    
    lista = []    
    
    for i in range(len(lista) - 1): 
        if lista[i + 1] != lista[i] + 1 :
            lista.append(lista[i] + 1)
            
    return lista