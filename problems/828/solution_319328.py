def primo(num):
    contador = 0
    for k  in range(1, num+1):
        if num % k == 0:
            contador += 1
    if contador != 2:
        return False
    else:
        return True