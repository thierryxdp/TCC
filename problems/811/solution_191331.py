def colchao (H,L):
    '''
    funçao que recebe as dimensoes de um colchao e as medidas da porta e
    retorna se é possivel passar por ela ou não
  
    list, int,int->bool
    '''
    result=bool
    if medidas [0] <= L and medidas[1]<=H :
        result = True
    elif medidas [1]<= L and medidas [0]<= H :
        result = True
        else :
            result = False
            return result