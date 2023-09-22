def filtra_pares(inteiros):
    """função que recebe uma tupla com quatro números inteiros, avalia quais são pares e retorna apenas estes na ordem que forma indicados.
    tupla(int,int,int,int)->tupla(int)
    Explicação: para saber se um número é par basta verificar se o resto de sua divisão por 2 é zero. Depois, basta analisarmos as possíveis combinações e retornar os inteiros pares dependendo de sua posição"""
    a=inteiros[0]
    b=inteiros[1]
    c=inteiros[2]
    d=inteiros[3]
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    elif a%2==0 and b%2==0 and c%2==0:
        return (a,b,c)
    elif a%2==0 and b%2==0 and d%2==0:
        return (a,b,d)
    elif a%2==0 and c%2==0 and d%2==0:
        return (a,c,d)
    elif b%2==0 and c%2==0 and d%2==0:
        return (b,c,d)
    elif a%2==0 and b%2==0:
        return (a,b)
    elif a%2==0 and c%2==0:
        return (a,c)
    elif a%2==0 and d%2==0:
        return (a,d)
    elif b%2==0 and c%2==0:
        return (b,c)
    elif b%2==0 and d%2==0:
        return (b,d)
    elif c%2==0 and d%2==0:
         return (c,d)
    elif a%2==0:
        return (a,)
    elif b%2==0:
        return (b,)
    elif c%2==0:
        return (c,)
    elif d%2==0:
        return (d,)
    else:
        return ()