def divisores1(n):
    divisores = []
    for i in range(1,n+1):
        if n%i == 0:
            list.append(divisores,i)
            i+=1
    return divisores

def primo(x):
    for n in range(1,x+1): 
        if len(divisores1(x))== 2:
            return True
        elif len(divisores1(x)) != 2:
            return False