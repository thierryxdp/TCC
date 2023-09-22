def primo(n):
    if n%2 == 0:
        return False
    else:
        i = 3
        while(i < n):
            if n%i == 0:
                return False
            i = i+1
        return True