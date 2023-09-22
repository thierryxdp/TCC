def soma_h(num):
    '''retorna a soma dos numeros da sequencia 1+(1/2)+...+(1/n)
    int->float'''
    a=1
    for i in range(2,num+1):
        a+=(1/i)
    return round(a,2)