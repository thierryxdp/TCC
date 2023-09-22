def filtra_pares(x,y,z,w):
    """Função em que dados 4 números inteiros x y z w retorna uma tupla contendo somente on números pares.
    int, int, int, int -> int,int,int,int"""
    if x%2 == 0:
        item1 = x
    else:
            x = 0
            item1 = x
    if y%2 == 0:
         item2 = y
    else:
	       y = 0
	        item2 = y
    if z%2 == 0:
        item3 = z
    else:
	    z = 0
	    item3 = z
    if w%2 == 0:
        item4 = w
    else:
	    w = 0
	    item4 = w
        
    return item1,item2,item3,item4