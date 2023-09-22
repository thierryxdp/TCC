#---------------------EXERCICIO 4---------------------

def soma_h(numero):
    '''retorna a soma de n termos elevados a -1
       int -> float'''

    soma = 0

    for contador in range(1,numero+1):
        soma += 1/contador
        
    return round(soma,2)