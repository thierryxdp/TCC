def colchao(medida,H,L):
    ''' '''
    
    passagem_porta= H*L
    
    face_colchao = medida[0]*medida[1]*medida[2]
    
    if face_colchao < passagem_porta:
        return True
    else:
        return False