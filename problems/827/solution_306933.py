def qtd_divisores(x):
    '''
    funcao calcula a quantidade de divisores de um numero x
    '''
    listax=[x]
    if x>0:
        for i in range(1,x//2+1):
            if x%i==0:
                list.append(listax,i)
        return len(listax)
    else:
        return 0