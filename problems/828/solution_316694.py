def primo(num):
    a=0
    for i in range(num):
        i+=2
        if num%i==0:
            a+=1
    if a==0:
        return True
    else:
        return False