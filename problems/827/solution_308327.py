def qtd_divisores(numero):
    #Contador de divisores, inicia com 0
    quantidade=0
    #Vai do 0 até o número
    for divisor in range(numero+1):
        #vê se o divisor é diferente de 0 e se o resto é zero
        if divisor !=0 and numero % divisor==0:
            #Incrementa 1 à quantidade de divisores
            quantidade+=1
    return quantidade