def soma_h(n):
    h = 1
    for i in range(n+1):
         if i !=0:
            h+=  i**(-1)
        return round(h,2)