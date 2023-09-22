def faltante (lista):
    """..."""
    lisordem=sorted(lista)
    lista2=lisordem[1:]
    for n in range(len(lista)-1):
        if lista2[n]-lisordem[n] != 1:
            return lista2[n] - 1