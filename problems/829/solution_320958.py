def soma_h(N: int):
    '''função que calcula e retorna o valor H com N termos onde N é inteiro
       e dado como entrada'''
    H=0
    for den in range(1,N+1):
        H=H+1/den
    return round(H,2)