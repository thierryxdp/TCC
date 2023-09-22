def qtd_divisores(num):
    '''Função que retorna quantos divisores o numero tem
    int -> int'''
    contador = 0
    
    for numero in range(1, num+1):
        if num % numero == 0:
            contador +=1
    if num < 0:
        return contador
    else:
        return contador