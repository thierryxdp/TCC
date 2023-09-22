def soma_h(n):
    'recebe uma soma H e retorna o resultado substituindo a variavel n'
    h = 1
    for i in range(n+1):
        if i !=0:
            h+= 1/i
    return round(h,2)