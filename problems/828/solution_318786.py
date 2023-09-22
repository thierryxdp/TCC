def primo(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0: 
        return False
    else: 
        for i in range(3, num // 2, 2):
            if num % i == 0:
                return False
            break
        else:
            return True