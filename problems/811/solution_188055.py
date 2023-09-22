def colchao(medidas, H, L):
    '''Funcao que dadas as medidas A,B e C (em ordem crescente)de um colchão, retornara True caso seja possivel passa-lo pela porta e False caso nao seja.'''
    if medidas[0]<L and medidas[1]<=H:
        return True 
    elif medidas[0]<L and medidas[1]>=H:
        return False 
    elif medidas[0]>L and medidas[1]<=H:
        return False 
    elif medidas[0]>L and medidas[1]>=H:
        return False
    else:
    import math    
    L=math.sqrt(H**2+L**2)
    c=math.sqrt((medidas[2]-L)/2)**2-((L/H)*10)**2
    n=c**2/(L/H)
    H2=n+(L/H)
    x=math.degrees(math.sin((H2/medidas[1])))
    if x>=0.656059 and x<=0.694658:
        return True
    else:
        return False