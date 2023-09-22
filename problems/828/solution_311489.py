def primo(n):
    multiplos = 0
    for count in range(2,n):
        if (n % count == 0):
            mult += 1
            return 'True'
        else:
            return 'False'