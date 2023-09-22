def qtd_divisores(num):
    """ a função calcula e retorna a quantidade de divisores que o numero de entrada
    tem;
    int->int"""
    d = []
    for i in range(1,num + 1):
        if num%i == 0:
            list.append(d,i)
    return len(d)