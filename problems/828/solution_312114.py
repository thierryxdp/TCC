def qtd_divisores(n):
    '''dado um número n, retorna quanros divisores esse número tem;
    int --> int'''
    lista=[]
    for num in range(1,n+1):
        if n%num==0:
            list.append(lista,num)
    for num in range(-n-1,0):
        if n%num==0:
            list.append(lista,num)
    return len(lista)

def primo(n):
    '''dado um número n, retorna se ele é primo ou não;
    int --> bool'''
    lista=[]
    if qtd_divisores(n)==4:
        return 2==2
    else:
        return 2==1