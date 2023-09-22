def qtd_divisores(numero):
    """Dado um numero, a função mostrará a quantidade
    de valores que a divisao resta 0. Caso o 
    numero seja negativo,o resultado será 0
    int->int"""
    resultado=[]
    if numero>0:
        for i in range(1,1000):
            if numero%i==0:
                list.append(resultado,i)
        return len(resultado)
    else:
        return 0