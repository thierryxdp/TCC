def colchao(medidas,H,L):
    """retorna se as medidas do colchao passam pela porta
    list->bool"""
    
    lista=[H,L]
    lista.sort()
    
    if medidas[0]<=lista[0] and medidas[1]<=lista[1]:
        return True
    else:
        return False