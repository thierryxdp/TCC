def soma_h(num):
    c = 0.0
    
    for i in range(1, num+1):
        c+= 1/i
    return round(c,2)