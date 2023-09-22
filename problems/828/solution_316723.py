def primo(n):
    a=0
    for i in range(n):
        if n%2==0 or n%3==0 or n%5==0:      
            a= False
        elif  n%17==0 or n%71==0:    
            a =False
        elif n%13==0 :
            a= False
        elif  n%1==0  and n%11==0 and n%221==0:
            a= False
        else:
            a=True
    return a