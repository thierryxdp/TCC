def faltante(lista):
    """determina o número faltando na lista;
    list -> int"""
      
    for contador in range(len(lista) - 1): 
        if lista[contador + 1] != lista[contador] + 1 :
            lista.append(lista[contador] + 1)
    return lista