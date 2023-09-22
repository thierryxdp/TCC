def (colchao,h,l):
	'''Determina se um objeto passa por uma porta com dimensões h e l dados altura largua e comprimento(medida[]) 
    lista, int, int --> bool'''
    if(colchao[0] <= l) and (colchao[1] <= h):
        return True
    else:
        return False