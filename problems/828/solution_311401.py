def primo(n):
    soma = 0
    for i in range(2, n):
        if n % i == 0 :
            if i % 2 == 0:
                continue
            return False
        else:     
            return True