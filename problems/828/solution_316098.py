def primo(n):
    divi = 0
    for num in range(1,n):
        if n % num == 0:
            divi += 1
            
    return divi < 2