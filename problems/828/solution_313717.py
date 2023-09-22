def primo(n):
    
    for count in range(2,n//2+1):
        if (n%count==0):
            return False