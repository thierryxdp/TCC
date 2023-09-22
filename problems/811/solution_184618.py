def colchao(medidas, H, L):
    '''Retorna se o colchão passa na porta ou não
    list / int / int i -> bool'''
    
    A, B, C = medidas.split()
    
    saida = 0
    
    if A <= H or A <= L:
        saida += 1
    if B <= H or B <= L:
        saida += 1
    if C <= H or C <= L:
        saida += 1
        
    if saida > 1:
        return True
    else:
        return False