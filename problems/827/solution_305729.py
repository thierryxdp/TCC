def qtd_divisores(num):
    """Função que retorna quantos divisores um numero tem
    int->int"""
    numeros_div = []
    for x in range(1,num+1):
        if num%x==0:
            list.append(numeros_div,x)
    return len(numeros_div)