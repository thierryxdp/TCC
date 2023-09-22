def qtd_divisores(x):
    """."""
    contador = 0
    
    for i in range(1,x):
        if i%x == 0:
            contador  += 1
    return contador