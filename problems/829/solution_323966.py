def soma_h(n):
    r=()
    for i in range(1,n):
        r=r+(1/i,)
        
    return round(sum(r),2)