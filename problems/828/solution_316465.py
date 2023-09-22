def primo(numero):
    for divisor in range(numero):
        if divisor != 0 :
            if divisor < numero and divisor !=1 and numero%divisor ==0:
                return False
    return True