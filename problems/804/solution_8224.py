def filtra_pares(a, b, c, d):
    lista = []
    
	if a / 2 == int(a / 2):
        lista += str(a)
    if b / 2 == int(b / 2):
        lista += str(b)
    if c / 2 == int(c / 2):
        lista += str(c)
    if d / 2 == int(d / 2):
        lista += str(d)
    	
    def convert(list):
   		return tuple(list)
    
    convert(lista)
        
    return tuple(lista)