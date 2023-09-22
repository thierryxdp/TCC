def qtd_divisores(v):
    '''retorna a quantidade de divisores do numero de entrada 
    int -> int'''
    a=1
    b=[]
    while a <= v:
        if(v%a==0):
            b=b+[a]
        a=a+1
    return b