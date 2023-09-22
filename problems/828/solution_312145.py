def primo(n):
    divisores = 0
    for i in range(1,n):
        if n%i==0 and 2<=i<n:
            divisores+= 1
            primo = 1 
        else:
            primo = 0
    return bool(primo)