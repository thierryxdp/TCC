def primo (n):
    """ funcao devera receber um numero e retornar true caso esse seja primo ou false caso nao seja
    entrada: int  saida:bool"""
    contador = 0
    for i in range(1,n+1):
        if n%i==0:
            contador = contador + 1
        if n%i != 0:
            contador = contador
    if contador == 2:
        return True
    else:
        return False