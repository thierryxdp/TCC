def soma_h(n):
    h = 0
    t = n
    for i in range(t):
        if i != 0:           
        	h = h+(1/i)
    return round(h,2)