def qtd_divisores(num):
    divisores=0
    for divisor in range(1,num+1):
        if num % divisor==0:
            divisores=divisores+1
            
    return divisores
def primo(num):
    if qtd_divisores(num) == 2:
        return True
    else :
        return False