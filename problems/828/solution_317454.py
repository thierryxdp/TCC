def primo(numero):
    ''' função que dado um número verifica se este numero é primo ou não.
        int ---> int '''
    quantidade_de_divisores = [1]
    a = numero
    for numero in range(1,a+1, 2):
        if a % numero == 0:
            list.append(quantidade_de_divisores, numero)
            numero -= 1
        else:
            numero -=1
    if len(quantidade_de_divisores) > 2:
        return False
    else:
        return True