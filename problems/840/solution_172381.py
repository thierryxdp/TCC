def bolos(a,b,c):
    2,3,5
    
    xi=(a-a%2)/2
    ov=(b-b%3)/3
    co=(c-c%5)/5
    
    if xi<ov and xi<co:
       return xi 
    if ov<xi and ov<co:
       return ov
    if co<ov and co<xi:
       return co