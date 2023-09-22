def primo (n):
    '''se o numeror tiver  dois divisores
    como 1 e ele mesmo, então é primo e retorna true'''
    if n != 0 & n != 1:
        if n > 3:
            for i in range(2, n):
                if n % i == 0:
                    return False
        return True