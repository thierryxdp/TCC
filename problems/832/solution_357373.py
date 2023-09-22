def eh_quadrada(lista):
    """Dada uma matriz, retorna True se a matriz for quadrada e False se não for"""
    """entrada: lista(lista)
    saida: booleano"""
    
    if len(lista) == len(lista[0]):
        return True
    
    elif len(lista) == 0:
        return True
    
    else:
        return False