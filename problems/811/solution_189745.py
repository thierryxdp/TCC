def colchao(medidas,H,L):
    ''' Funcao que calcula se o colchao consegue 
        passar pelas portas de acordo com as medidas
        list, , int, int -> bool 
    ''''
    if medidas[1] <= H:
       return True
    elif medidas[1] <= L:
       return True
    elif medidas[2] >=H:
       return False