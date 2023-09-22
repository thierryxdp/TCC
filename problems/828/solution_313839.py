def primo(n):
    
    for count in range(1,n+1):
        if (n % count == 0):
            mult += 1
        if(mult==0):
            return n