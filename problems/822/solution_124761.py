def repetidos(lista:list)->int:
    rep = 0
    lista_atras = lista[:-1]
    lista_frente = lista[1:]
    for a,b in zip(lista_atras,lista_frente):
        if a == b:
            rep+=1
    return rep