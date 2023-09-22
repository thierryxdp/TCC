def filtra_pares (a,b,c,d):
    '''Função para retornar os numeros pares dados 4 números inteiros
    int -> int'''
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return a,b,c,d
    elif a%2 != 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return b,c,d
    elif a%2 != 0 and b%2 != 0 and c%2 == 0 and d%2 == 0:
        return c,d
    elif a%2 != 0 and b%2 != 0 and c%2 != 0 and d%2 == 0:
        return d
    elif a%2 != 0 and b%2 != 0 and c%2 != 0 and d%2 != 0:
        return "Não há elementos pares"