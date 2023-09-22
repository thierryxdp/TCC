def primo(n):
    divisores=0
    for i in range(n):
        if n%i==0:
            divisores+=1
            print(divisores)