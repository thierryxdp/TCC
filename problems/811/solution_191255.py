def colchao(medidas,H,L):
    '''
    função que calcula se é possível passar um colchão pelas portas de uma residencia, de 
    tal forma que uma de suas faces passe paralela ao chão. É informado na entrada uma lista 
    com as dimensões do colchão em centimetros, ordenadas da menor para a maior, e dois números 
    inteiros 
    list,int,int->
    medidas=[A,B,C]
    '''
   
    if medidas[1]<= H and medidas[0]<=L:
        return True

    elif medidas[2]<=H and medidas[0]<=L:
        return True
    
    else:
        return False