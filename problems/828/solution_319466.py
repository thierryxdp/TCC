def primo(n):
    for i in range(2,n):
        if (n % i == 0):
            m += 1
        if(m==0):
            return True
        else:
            return False