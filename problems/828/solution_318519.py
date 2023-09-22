def primo(n):
    prime=False
    divisores=0
    for numero in range(2,n//2+2):
        if n%numero==0:
            divisores+=1
    if divisores==0:
        prime=True
    return prime