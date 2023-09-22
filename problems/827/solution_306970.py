def qtd_divisores(numero):
    ''' recebe um numero e ve a qunatidade de divisores que esse numero possui
    int->int'''
    numeros_totais: []
    for i in range(0,numero + 1):
        if numero%i == 0:
            list.append(numeros_totais,i)
    return len(numeros_totais)