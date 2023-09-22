def colchão(x,H,L):
    '''
    função que calcula se é possível passar um colchão pelas portas de uma residencia, de 
    tal forma que uma de suas faces passe paralela ao chão. É informado na entrada uma lista 
    com as dimensões do colchão em centimetros, ordenadas da menor para a maior, e dois números 
    inteiros 
    list,int,int->
    x=[A,B,C]
    '''
   
    if x[1]<= H and x[0]<=L:
        return True

    elif x[2]<=H and x[0]<=L:
        return True
    
    else:
        return False