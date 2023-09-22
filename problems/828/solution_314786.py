def primo(num):
    som=0
    for i in range(2,num):
        if num%i==0:
            som=som+1
    if som>0:
        return False
    else: 
        return True