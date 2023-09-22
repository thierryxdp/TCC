def fatorial(n):
    i     = 1  # contador
    n_fat = 1  

    # calcule n!
    while i <= n:
        n_fat = n_fat * i 
        i = i + 1

    return n_fat