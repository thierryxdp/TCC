def primo(n):
    
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1