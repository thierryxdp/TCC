def primo(num):
    boll = 0
    for i in range(2,num):
        if num%i==0:
            boll=True
        elif num%i!=0:
            boll=False
        
    return boll