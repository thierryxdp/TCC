def qtd_divisores(n):
    r = []
    l = (range(n+1)) 
    for i in l:
        if n%i==0:
            r = r.append(i)
    
    return len(r)