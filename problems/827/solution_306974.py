def qtd_divisores(num):
    ''' recebe um numero e ve a qunatidade de divisores que esse numero possui
    int->int'''
    numeros_totais= []
    for i in range(1,int(num+1)):
        if num % i == 0:
            list.append(numeros_totais,i)
    return len(numeros_totais)