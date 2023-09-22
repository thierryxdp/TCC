def primo(n):
    ''' funcao que dado um numero retorna se ele é primo ou nao. int --> bool'''
    contador = 0
    for divisor in range(n+1):
        if divisor != 0:
            if n%divisor ==0:
                contador += 1
    if contador > 2:
        return False 
    if contador <= 2:
        return True