def primo():
    """Função que dado o número inteiro positivo, verifique
    se este número é primo ou não.
    int -> int"""
    num = int(input('Digite um número:'))
    for c in range(1, num + 1):
        if num % c == 0:
            return ('\033[33m', end='')
            tot += 1
        else:
            return ('\033[31', end='')
        return ('{}'. format(c), end="")
    return ('\n\033\[m0 número {} foi divisível {} vezes'. format(num, tot))
    if tot == 2:
        return ("True")
    else:
        return ("False")