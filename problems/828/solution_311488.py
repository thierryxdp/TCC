def primo(n):
    for count in range(2,n):
        if (n % count == 0):
            return 'True'
        else:
            return 'False'