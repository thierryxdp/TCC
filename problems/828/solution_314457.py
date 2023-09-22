def primo(num):
    som=0
    for i in range(2,num+1):
        if num%i==0:
            som=som+(num%i)
            if som==0:    
                return False
        else:
            return True