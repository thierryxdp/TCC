def soma_h(n):
    H=0
    round(H,2)
    for i in range(n):
        if n==1:
            H= 1
        if n==5:
            H= 1+1/2+1/3+1/4+1/5
        if n==6:
            H= 1+1/2+1/3+1/4+1/5+1/6
        if n==10:
            H= 1+1/2+1/3+1/4+1/5+1/6+1/7+1/8+1/9+1/10
                  
    return round(H,2)