def soma_h(n):
    '''funcao que recebe um numero inteiro e retorna 
       o resulado da soma 
       int -> float'''
    i= 0
    soma= 0
    for x in range(n):
        soma += 1/(i+1)
        i+= 1
    return round(soma,2)