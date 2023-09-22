def colchao(medidas,H,L):
    
    """Funçao que calcula e retorna se o colchao passa pela porta de medidas dadas"""
    
    if medidas[0] < L and medidas[1]<=H:
        
        return True
    
    else:
        
        return False