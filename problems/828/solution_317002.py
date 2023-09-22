def primo(n):
    i= 0
    for x in range(n):
        if n%1 == 0 and n%n == 0 and n%[i+1] != n[i]:
            return True 
        else:
            return False
        i+= 1