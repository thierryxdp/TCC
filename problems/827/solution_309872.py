def qtd_divisores(n):
    lista = []
    for i in range( n//2+1):
        if n % i ==0:
            lista.append(i)
    return len(lista)