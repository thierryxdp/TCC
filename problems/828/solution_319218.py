def primo(num):
    if num < 2:
        return 'Não é primo.'
    else:
        for n in range(2,num):
            if num % n ==0:
                return 'Não é primo.'
            return 'É primo.