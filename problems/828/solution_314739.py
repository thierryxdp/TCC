def primo(num):
    '''dado um numero inteiro e positivo, verifica se ele e primo
    ou nao
    int -> bool'''
    
    a=1
    b=0
    
    while a<=num:
        if num%a==0:
            b+=1
        a+=1
    if b==2:
        return True
    else:
        return False