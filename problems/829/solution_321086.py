#---------------------EXERCICIO 4---------------------

def soma_h(lista_numeros):
    '''retorna a soma de n termos elevados a -1
       list -> int'''

    soma = 0

    for contador in lista_numeros:
        soma += 1/contador
        
    return round(soma,2)