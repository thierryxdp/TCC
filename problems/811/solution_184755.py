def colchao(medida,h,l):
	'''Determina se um objeto passa por uma porta com dimensões h e l dados altura largua e comprimento(medida[]) 
    lista, int, int --> bool'''
    if(medida[0] <= l) and (medida[1] <= h):
        return True
    elif(medida[0] <= h) and (medida[2] <= l):
         return True
    else: 
         return False