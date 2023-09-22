#int->bool
def primo(num):
    #essa função retornará se o número é primo ou não
    contador = 0
    for k  in range(1, num+1):
        if num % k == 0:
            contador += 1
    #por definição, um número é primo se ele tiver o numero de divisores igual a 2
    if contador != 2:
        return False
    else:
        return True