def primo(n):
    divisores = 0
    for i in range(1,n):
        if n%i==0 and 2<=i<n:
            div+= 1
            primo = 1 
        else:
            div = 0
            primo = 0
    return bool(div)