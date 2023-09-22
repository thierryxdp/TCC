def primo(num):
    contador=0
    for i in range(1,num+1):
        if i%num==0:
            contador+=1
        if contador<=2:
            return True
        else:
            return False