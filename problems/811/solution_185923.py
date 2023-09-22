def colchao(medidas,H,L):
    '''Calcula e retorna se um colchao de medidas dadas como valor de entrada
       passa por uma porta de medidas H e L também dadas;
       list, int, int -> bool'''
    
    lados_menores = 0
    
    for n in medidas:
        
        if n <= H or n <= L:
            
            lados_menores += 1
            
    if lados_menores >= 2:
        
        return True
    
    else:
        
        return False