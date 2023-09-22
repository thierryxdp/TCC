def primo(num):
    '''Dado um número inteiro positivo, retorna se este número é primo ou não;
    int -> boolean'''

    if num == 2:
        return True

    elif num < 2 or num%2 == 0:
        return False

    else:
        for d in range(3,num//2 +1,2):
            div.append(d)
            if num % d == 0:
                return False
        return True