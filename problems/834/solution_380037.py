def media_matriz(media):
    
    mat0= 0
    mat1= len(media)
    mat2= len(media[0])
    final1= (mat1)*(mat2)
    
    for a in range (mat1):
        for b in range(mat2):
            mat0= mat0+ mat0[a][b]
              
    final2= mat0/final1
            
    return round(final2,2)