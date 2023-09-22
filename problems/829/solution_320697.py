def soma_h(n):
    sequencia = list(range(1,n+1))
    h=0
    
    for i in sequencia:
        h= h + (1/i)
        
	return round(h,2)