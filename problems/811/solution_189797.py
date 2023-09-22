def colchao(medida,H,L):
    ''' '''
    
    passagem_porta= H*L
    
    face_colchao = medida[0]*medida[1]
    
    if face_colchao < passagem_porta and medida[1] <= H:
        return True
    else:
        return False