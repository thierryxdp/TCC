#---------------------EXERCICIO 4---------------------

def soma_h(numero):
    '''retorna a soma de n termos elevados a -1
       list -> int'''

    lista_numeros = range(1,numero+1)
    soma = 0

    for contador in lista_numeros:
        soma += 1/contador
        
    return round(soma,2)