def primo(n):
    '''recebe um numero inteiro e retorna TRUE para numeros
    primos e FALSE para numeros nao primos.
    entrada: int
    saida: booleano'''
    Nprimos=0
    for c in range(2,n):
        if n % c == 0:
            Nprimos+=1
    if Nprimos==0:
        return True
    else:
        return False