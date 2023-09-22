def primo(n):
    contador = 0
    for numero in range(2, n):
        if (n % numero  == 0):
            contador += 1

            if contador == 0:
                return True
            if contador > 0
                return False