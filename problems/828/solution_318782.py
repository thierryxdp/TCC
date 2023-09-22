def primo(num):
    if num < 2:
        return 'não é primo'
    elif num == 2:
        return 'primo'
    elif num % 2 == 0: 
        return 'não é primo'
    elif: 
        for i in range(3, num // 2, 2):
            if num % i == 0:
                return 'não é primo'
        else:
            return 'é primo'