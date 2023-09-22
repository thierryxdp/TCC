def acima_da_media(lista_notas:list,média:int)->list:
    """Dada uma lista ordenada de números int, inclui n na posição correta, de forma que a lista contuinue ordenada."""
    lista_notas.append(n)
    lista_notas.sort()
    num = lista_notas.index(n)
    del lista_notas[0:num+1]
    return lista_notas