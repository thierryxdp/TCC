def colchao(medida,H,L):
    '''Essa função retorna se um coixão, dado suas 3 medidas de altura largura e comprimento,
    consegue passar por uma porta, dado dado sua altura e largura
    list[int,int,int],int,int -> bool'''
    
    passagem_porta= H*L
    
    face_colchao = medida[0]*medida[1]
    
    if face_colchao <= passagem_porta and medida[1] <= H:
        return True
    elif face_colchao <= passagem_porta and medida[1] <= L:
        return True
    else:
        return False