def primo(num):
    multi=0
    for num_primo in range(1,num+1):
        if num% num_primo==0:
            multi+=1
    if multi==2:
        return True
    elif:
        return False