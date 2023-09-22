def soma_h(numero):
    H=0
    s=1
    for i in range(1:numero+1):
        H=H+(1/s)
        s=s+1
    return H