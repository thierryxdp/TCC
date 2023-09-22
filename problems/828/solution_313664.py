def primo(n): 
    tot = 0
    for x in range(1,n+1):
        if x%n==0:
            tot += 1            
        elif tot<=2:
            return True