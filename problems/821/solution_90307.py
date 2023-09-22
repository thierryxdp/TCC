def fatorial(n):
    "Recebe um numero e retorna o fatorial deste numero"
    "entrada: int. saida: int"
    if n<=1:
        return 1
    else:
        return n*fatorial(n-1)