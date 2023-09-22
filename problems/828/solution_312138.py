def primo(n):
    for i in range(1,n):
        if 2<=i<n and n%i ==0:
            primo = 1 
        else:
            primo = 0
    return bool(primo)