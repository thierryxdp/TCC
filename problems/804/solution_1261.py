# Função que dado quatro números filtra apenas os números pares
# Parameters: 
# entrada1: primeiro número dado, entrada2: segundo número dado, 
# entrada3: terceiro número dado, entrada4: quarto número dado
# float, float, float, float -> tuple

def filtra_pares (entrada1, entrada2, entrada3, entrada4):
    a = entrada1 // 2
    b = entrada2 // 2
    c = entrada3 // 2
    d = entrada4 // 2
    
    if a == b == c == d == 0:
        return (entrada1, entrada2, entrada3, entrada4)
    elif a and b != 0:
        return (entrada3, entrada4)
    elif a and c != 0:
        return (entrada2, entrada4)
    elif a and d != 0:
        return (entrada2, entrada3)
    elif b and c != 0:
        return (entrada1, entrada4)
    elif b and d != 0:
        return (entrada1, entrada3)
    elif c and d != 0:
        return (entrada1, entrada2)
    elif d != 0:
        return (entrada1, entrada2, entrada3)
    elif c != 0:
        return (entrada1, entrada2, entrada4)
    elif b != 0:
        return (entrada1, entrada3, entrada4)
    elif a != 0:
        return (entrada2, entrada3, entrada4)
    else
    return ()