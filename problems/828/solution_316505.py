def primo(num):
    ''' dado um numero inteiro e positivo(num)
    a funcao verifica se é primo
    int -> bool'''

    for x in range(2,num+1):
        if num != x and num % x == 0:
            return False
        if num % x == 0 and num == x:
            return True