def primo(num):
    '''função que define se um número escolhido,num, é um número primo ou não'''
    x=0
    a=list(range(1,num+1))
    for i in a:
        if num%i==0:
            x=x+1
    return x=2