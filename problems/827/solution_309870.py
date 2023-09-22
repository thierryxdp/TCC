def qtd_divisores(n):
    lista = [1]
    for i in range(1, n//2+1):
        if n % i ==0:
            lista.append(i)
    return len(lista)