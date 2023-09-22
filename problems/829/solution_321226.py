def soma_h(n):
    i=0
    h=0
    for i in range(1,n+1):
        i+=1/i
        h+=1/(n+1-i)
        return i