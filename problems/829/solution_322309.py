def soma_h(N):
    '''funcao que dado um valor N, este sendo um numero inteiro positivo, retorna o valor H da soma de 1 sobre todos os numeros de 1 ate N;
       int->float'''
    valorH= 0
    for n in range(N):
        if n!=0:
            valorH= valorH+ 1/n
    return round(valorH,2)