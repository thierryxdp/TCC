def qtd_divisores(n):
    '''retorna o números de divisores do inteiro n'''
    if n<0:
        return 0
    '''obs*: discordo que o resultado esperado para números negativos seja 0'''
    qtd=sum(map(i:n%i==0,range(1,n//2+1)))+1
    return qtd