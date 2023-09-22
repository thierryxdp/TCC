def primo(numero):
    'recebe um número e retorna um booleano que indica se ele é primo ou não'
    for divisor in range(numero):
        if divisor != 0 :
            if divisor < numero and divisor !=1 and numero%divisor ==0:
                return False
    return True