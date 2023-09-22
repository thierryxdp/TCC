def filtra_pares(tup):
        n1 = int(tup[0])
        n2 = int(tup[1])
        n3 = int(tup[2])
        n4 = int(tup[3])

        if n1%2 == 0 and n2%2 == 0 and n3%2 == 0 and n4%2 == 0:
            return tuple(tup)
    
        elif n1%2 > 0 and n2%2 > 0 and n3%2 > 0 and n4%2 > 0:
            return tuple()
    
        elif n1%2 == 0 and n2%2 == 0 and n3%2 == 0:
            return n1,n2,n3
    
        elif n1%2 == 0 and n3%2 == 0:
            return n1, n3
    
        elif n1%2 == 0 and n2%2 == 0:
            return n1, n2
    
        elif n2%2 == 0 and n3%2 ==0:
            return n2, n3
    
        elif n3%2 == 0 and n4%2 == 0:
            return n3,n4
        
        elif n2%2 == 0 and n3%2 == 0 and n4%2 ==0:
            return n2,n3,n4
        
		elif n4%2 == 0:
            return n4