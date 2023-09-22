def soma_h(n):
    'recebe uma soma H e retorna o resultado substituindo a variavel n'
    h = 1
    for i in range(n+1):
        if i !=0:
            h += i**(-1) 
            h = h-1
    return round(h,2)