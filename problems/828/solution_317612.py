def primo(num):
    boll = 0
    for i in range(2,num):
        if num%i==0:
            boll=True
        else:
            boll=False
    return boll
    
#primo(228)