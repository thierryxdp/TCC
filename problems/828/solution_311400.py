def primo(n):
    soma = 0
    for i in range(2, n):
        if n % i == 0 :
            return False
        else:
            if i % 2 == 0:
                continue
            else:
                i
        return True