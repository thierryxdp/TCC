def primo(n):
    m= 0
    for i in range(0,n):
        if (n % i == 0):
            m += 1
        if(m==0):
            return True
        else:
            return False