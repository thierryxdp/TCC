def colchao(medidas,H,L):
    """Função que retorna true caso o colchão passe pela
    porta e false caso contrário, dados como entrada as 
    medidas, a altura 'H' e a largura 'L' """
	
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if A<L and B<=H or B<L:
        return True
    else:
        return False