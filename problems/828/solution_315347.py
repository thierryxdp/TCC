def primo(n):
    '''Uma função dado um inteiro retornar se é primo ou não
    int -> booleano'''
divisores = 0
for divisor in range(1, numero):
    if numero % divisor == 0:
        divisores = divisores + 1
        if divisores > 1:
          break
if divisores > 1:
    return False
else:
    return True