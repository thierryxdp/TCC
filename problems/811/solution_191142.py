def colchao(medidas,H,L):
    ''' Função que retorna True se for possível passar o colchão de medidas
    A x B x C pela porta de medidas H x L, e False se não for possível
    list,int,int -> bool '''
    
    import math
    diagonal_porta = math.sqrt((H**2)+(L**2))
    if diagonal_porta >= medidas[1] and L >= medidas[1] and H <= medidas[2]and medidas[1] <= H :
        return True
    else:
        return False