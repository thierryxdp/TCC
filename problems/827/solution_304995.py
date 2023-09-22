def qtd_divisores(x):
    lista = []
    for n in range(1, x+1):  
        if(x % n  == 0):
            lista.append(n)
    return len(lista)