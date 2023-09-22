def filtra_pares(x):
    (a, b, c, d) = x
    nova_tupla = ()
    if a%2 == 0:
        return nova_tupla + ((a,))
    	if b%2 == 0:
        	return nova_tupla + ((b,))
    		if c%2 == 0:
        		return nova_tupla + ((c,))
    			if d%2 == 0:
        			return nova_tupla + ((d,))
    				if a%2 == 0 and b%2 == 0:
        				return nova_tupla + ((a,)) + ((b,))
    					if a%2 == 0 and c%2 == 0:
        					return nova_tupla + ((a,)) + ((c,))
    						if a%2 == 0 and d%2 == 0:
        						return nova_tupla + ((a,)) + ((d,))
    							if b%2 == 0 and c%2 == 0:
        							return nova_tupla + ((b,)) + ((c,))
    								if b%2 == 0 and d%2 == 0:
        								return nova_tupla + ((b,)) + ((d,))
    									if c%2 == 0 and d%2 == 0:
        									return nova_tupla + ((c,)) + ((d,))
    										if a%2 == 0 and b%2 == 0 and c%2 == 0:
        										return nova_tupla + ((a,)) + ((b,)) + ((c,))
    											if a%2 == 0 and b%2 == 0 and d%2 == 0:
        											return nova_tupla + ((a,)) + ((b,)) + ((d,))
    												if b%2 == 0 and c%2 == 0 and d%2 == 0:
        												return nova_tupla + ((b,)) + ((c,)) + ((d,))
    													if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        													return nova_tupla + ((a,)) + ((b,)) + ((c,)) + ((d,))
        
    
    return nova_tupla