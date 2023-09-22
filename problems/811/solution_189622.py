def colchao(medida,h,l):
    '''Funçao que calcula se um objeto passa por uma porta
   	   Parametros h:altura
       			  l:largura
                  comprimento: (medida[])'''
    if (medida[0] <= h) and (medida[1] <= h):
        return True
    elif (medida[0] <= h) and (medida[1] <= l):
        return True
    else:
        return False