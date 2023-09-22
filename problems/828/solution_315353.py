def primo(num):
    verifica=0
    for i in range(2,num):
        if num%i==0:
            verifica+=1
    if verifica==0:
        return True
    else:
        return False