def primo(num):
    
    for i in range(2,num+1):
        if (num%i==0)and i!=num and i!=1 and i>=num:
            return False
        else:
            return True