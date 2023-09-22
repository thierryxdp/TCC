def primo(p):
    n = 1
    m = 1
    while n**2 <= p:
        m = m*n
        n = n+1
    
    return p%n==0