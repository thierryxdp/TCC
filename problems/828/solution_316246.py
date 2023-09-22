def primo(num):
    
    contador=0
    
    for x in range(2,num):
        
        if num%x!=0:
            contador=contador+1
            return True
        if num%x==0:
            return False