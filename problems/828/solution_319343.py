def primo(num):
    contador=0
    while point<=num//2:
        if num%point==0:
            contador+=1
    if contador!=0:
        return False
    else:
        return True