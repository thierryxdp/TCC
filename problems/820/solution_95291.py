def posLetra(frase,letra,num):
    """..."""
    if str.count(frase,letra) >= num:
        return 'sla'
    else:
        return -1