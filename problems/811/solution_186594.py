def colchao(medidas,H,L):
    '''Função que, dada uma lista com as dimensões 
       em ordem crescente de um colchão, bem como 
       a altura e largura de uma porta, necessariamente 
       nessa ordem e com todas as medidas em valores 
       inteiros e em centímetros, informa se o colchão 
       consegue passar pela porta. 
       list, int, int -> bool'''
    
    A, B, C = medidas
    
    condicao1 = H > A and L > B
    condicao2 = H > A and L > A 
    condicao3 = L > B and H > C
    
    if condicao1 or condicao2 or condicao3:
        return True
    else:
        return False