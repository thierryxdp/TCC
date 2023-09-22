def soma_h(n):
    """ para calcular e retornar o valor de h com n termos, sendo 
    n um número inteiro, digite;
    int-> float"""
    h=0
    for i in range(1,n+1):
        h+= 1/i
    return round (h,2)