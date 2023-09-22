def faltante (list):
    """..."""
    lisordem=sorted(lista)
    lista2=lisordem[1:]
    for n in range(len(lista)):
        if lista2[n]-lisordem[n] != 1:
            return lista2[n] - 1