def primo(n):
    '''Função verifica se um dado número n é primo;
    int -> bool'''
    primos = []
    for i in range(1,n+1):
        cont=0
        for e in range(1,n+1):
            if i%e==0:
                cont += 1
        if cont==2:
            primos.append(i)
    return n in primos