def filtraMultiplos (meus_numeros,nova_lista):
    """
    
    """
    meus_numeros = [a, b, c, d, e, f, g, h, i, j]
    nova_lista = [numero for numero in meus_numeros if numero % 3 == 0]
    return(nova_lista)