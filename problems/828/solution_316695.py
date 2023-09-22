def primo(num):
    a=0
    for i in range(2,num):
        
        if num%i==0:
            a+=1
    if a==0:
        return True
    else:
        return False