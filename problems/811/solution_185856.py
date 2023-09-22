def colchao(medidas,H,L):
    """A função usará dos parâmetros de entrada para verificar
    a possibilidade  de um colchão passar pela porta, no caso
    afirmativo a função indicará True, no contrário False.
    Enquanto o elemento medida indicará 3 dimensões para 
    calcular o tamanho do colchão, os elementos 'H' e 'L' 
    representam, respectivamente, a altura da porta e o seu 
    comprimento.
    Entrada: Int, Int, Int
    Saída: Bool"""
  
    
    A,B,C = medidas
    medidas = A*B*C
    
    if A and B < max(H,L):
        return True
        
    if A and C < max(H,L):
        return True
    
    if B and C < max(H,L):
        return True
  
    else:
        return False