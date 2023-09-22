def soma_h(valor):
    '''retorna a funcao que calcula a soma de todas fraçoes,sendo
    os denominadores somados até o valor dado na entrada, obs o 
    numerador sempre será 1
    list->float'''
    soma=0
    for numero in list(range(valor+1)):
        if numero!=0:
            divisao=1/numero
            soma= divisao+soma
    return round(soma,2)