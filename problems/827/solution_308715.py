def qtd_divisores(n):
    numeros=[]
    qtd=0
    for i in range(1,n):
        if n%i == 0:
            qtd += 1
            
    return len(numeros)