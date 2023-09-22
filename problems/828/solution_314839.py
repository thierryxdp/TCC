def primo(num):
    '''recebe um numero e verifica se ele é primo ou não
    int->'''
    divisores=[]
    for i in range(1,int(num+1)):
        if num % i == 0:
            list.append(divisores,i)
    if divisores == [1,num]:
        return True 
    else:
        return False