def qtd_divisores(x):

    contador = 0
    c = 1
    

    while x/c > 1:
        if x%c == 0:

            c += 1
            contador += 1
            
    return contador