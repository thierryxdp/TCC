def qtd_divisores (n):
    ''' Dado um numero n, retorna quantos divisores esse numero tem'''
    i=n
    for i in range(1,n+1):
        if n%i == 0:
            lista = n%i==0
            
            return lista