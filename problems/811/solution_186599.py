def colchao(medidas,H,L):
    '''Função que, dada uma lista com as dimensões 
       em ordem crescente de um colchão, bem como 
       a altura e largura de uma porta, necessariamente 
       nessa ordem e com todas as medidas em valores 
       inteiros e em centímetros, informa se o colchão 
       consegue passar pela porta. 
       list, int, int -> bool'''
    
    A, B, C = medidas
    
    condicao1 = H > C and (L > B or L > A)
    condicao2 = H > B and (L > C or L > A)
    condicao3 = H > A and (L > C or L > B)
    
    
    if condicao1 or condicao2 or condicao3:
        return True
    else:
        return False