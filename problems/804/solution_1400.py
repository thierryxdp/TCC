# Função que dado 4 números quaisquer, retorna uma tupla com apenas os números pares
# entrada1: primeiro número, entrada2: segundo número, entrada3: terceiro número, entrada4: quarto número
# float, float, float, float -> tuple
def filtra_pares(entrada1, entrada2, entrada3, entrada4):
    a = entrada1 % 2
    b = entrada2 % 2
    c = entrada3 % 2
    d = entrada4 % 2
    
    if a != 0 and b != 0 and c !=0 and d !=0:
        return ()
    elif (a == b != 0) and (c == d == 0):
        return (entrada3, entrada4)
    elif (a == c != 0) and (b == d == 0):
        return (entrada2, entrada4)
    elif (a == d != 0) and (b == c == 0):
        return (entrada2, entrada3)
    elif (b == c != 0) and (a == d == 0):
        return (entrada1, entrada4)
    elif (b == d != 0) and (a == c == 0):
        return (entrada1, entrada3)
    elif (c == d != 0) and (a == b == 0):
        return (entrada1, entrada2)
    elif d != 0 and (a == b == c == 0):
        return (entrada1, entrada2, entrada3)
    elif c != 0 and (a == b == d == 0):
        return (entrada1, entrada2, entrada4)
    elif b != 0 and (a == c == d == 0):
        return (entrada1, entrada3, entrada4)
    elif a != 0 and (b == c == d == 0):
        return (entrada2, entrada3, entrada4)
    elif a == 0  and (b == c == d != 0):
        return (entrada1)
    elif b == 0 and (a == c == d != 0):
        return (entrada2)
    elif c == 0 and (a == b == d != 0):
        return (entrada3)
    elif d == 0 and (a == b == c != 0):
        return (entrada4)
    elif a == b == c == d == 0:
        return (entrada1, entrada2, entrada3, entrada4)