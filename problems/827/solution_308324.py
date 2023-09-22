def qtd_divisores(num):
    '''int -> int'''
    x=[]
    for div in list(range(num,0,-1)):
        if num % div == 0:
            list.append(x,div)
    return len(x)