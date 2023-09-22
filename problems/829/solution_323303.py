def soma_h(n):
    #define o valor de h
    h = 1
    #Percorre todos os números de 0 até n
    for i in range(n+1):
        #verifica se o i é diferente de zero
        if i !=0:
            h+=  i**(-1)
    return round(h,2)