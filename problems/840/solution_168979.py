def bolos(a,b,c):
    
    '''funcao que diz a quantidade de bolos possiveis 
    com determinados ingredientes'''
    boloc = (a//2,b//3,c//5)
    
    return min(boloc)