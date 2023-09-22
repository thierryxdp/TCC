def primo(num):
    
    contador=1
    for contador in range(1,num):
        if num%2==1:
            contador=contador+1
            return True
        
        else:
            return False