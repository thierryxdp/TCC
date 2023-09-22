def fatorial(numero):
    i     = 1  # contador
    n_fat = 1  

    while i <= numero:
        n_fat = n_fat * i 
        i = i + 1

    return n_fat