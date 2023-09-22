def colchao(medidas,H,L):
    '''
       A função recebe as medidas do colchao e da porta 
       e retorna True quando o colchao passa pela porta e
       False quando não é possível passar o colchao pela 
       porta
       list, int, int -> bool
    '''
    medias = [A, B, C]
    area_paralelepipedo = 2*A*B+2*B*C+2*A*B
    area_porta = H*L
    if area_paralelepipedo <= area_porta:
        return True
    else:
        return False