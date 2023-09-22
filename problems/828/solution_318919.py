def primo(num):
    contador=0
    for d in range(2,num-1):
        if num%d!==0:
            contador+=1
    if contador!=0:
        return False
    return True