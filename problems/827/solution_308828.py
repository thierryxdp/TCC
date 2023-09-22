def qtd_divisores (n):
    ''' Dado um numero n, retorna quantos divisores esse numero tem'''
    div=[]
    for i in range(1,n+1):
        if n%1==0:
            div.append(i)
        k=len(div)
        return k