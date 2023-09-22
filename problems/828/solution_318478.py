def primo(n):
    if (n <= 0):
        return false
    else:
        num_div = 0
        for i in range(1, n + 1):
            if (n % i == 0):
                num_div += 1
            
        if (num_div == 2):
            return true
        else:
            return false