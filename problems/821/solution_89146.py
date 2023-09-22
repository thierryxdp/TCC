def fatorial(n): 
    i=n
    resultado=0 
    while i == 1:
        if n*i:
            resultado=resultado+n*i
        i=i-1 
    return resultado