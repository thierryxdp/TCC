def primo(n): 
    tot = 0
    for x in range(1,n+1):
        if x%n=>2:
            tot += 1             
        else:
             return False
        if x%n==0:
            tot += 1   
        if tot<=2:
            return True