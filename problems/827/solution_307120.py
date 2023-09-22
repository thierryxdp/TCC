def qtd_divisores(numero):
    
    i = 1
    divisores = []
    while i <= numero:
        if numero%i == 0:
            divisores += [i]
    i += 1 
    return len(divisores)