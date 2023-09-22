def primo(n):
    '''Diz se um numero inteiro é ou não primo;
    int -> bolean'''
    divisores = list(range(2,n))#lista com numeros de 2 até n - 1
    divisor = 0 #numero que dividira n
    contador = 0
    if n == 2:
        return True
    for divisor in divisores:
        if n % divisor == 0:
           contador = contador + 1
    if contador == 0:#Se o contador for igual a zero significa que ele não é divisivel por nenhum numero
       return True

    if contador != 0:#Se o contador for igual a zero significa que ele é divisivel por algum numero
        return False