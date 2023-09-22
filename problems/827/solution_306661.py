def qtd_divisores(num):
    '''Funcao que retorna a quantidade de divisores de um dado
    numero inteiro. 
    Int -> Int'''
    quantidade= 0
    for i in range(1,num+1):
        if num%i == 0:
            quantidade += 1
    return quantidade