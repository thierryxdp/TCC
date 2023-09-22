def primo(n): 
    for x in range(1,n+1):
        tot = 0
        if x%n==0:
            tot = tot + 1            
    if tot>2:
        return True