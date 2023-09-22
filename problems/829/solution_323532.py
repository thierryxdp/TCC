def soma_h(numero):
    h=0
    for c in range(numero):
        h+=1/(c+1)
    return round(h,2)