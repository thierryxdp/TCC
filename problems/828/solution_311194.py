def primo(n):
    for num in range(2,n):
        if n%num == 0:
            return False
    else: 
        return True