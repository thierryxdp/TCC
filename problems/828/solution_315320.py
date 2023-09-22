def primo(num):
    numero=0
    for i in range(1,num+1):
        if num % i== 0:
            numero=numero+1 
    if numero>2 or numero==1:
        return False
    else:
        return True