def def qtd_divisores(num):
    seq=list(range(1,num+1))
    divisores=[]
    for i in seq:
        if num%i==0:
            divisores.append(i)
    return len(divisores)

def primo(num):
    '''A funcao recebe um numero e identifica se ele e primo ou nao int->bool'''
    if qtd_divisores(num)==2:
        return True
    else:
        return False