def primo(num):
    divisores=[]
    for i in range(1:num+1):
        if num%i==0:
            list.append(divisores,i)
    if len(divisores)!=2:
        return False
    else:
        return True