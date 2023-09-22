def filtraMultiplos ():
    """
    
    """
    meus_numeros = [1, 56, 342, 12, 781, 23, 43, 45, 123, 567]
    nova_lista = [numero for numero in meus_numeros if numero % 3 == 0]
    return(nova_lista)