def soma_h(N):
    '''Função que dado um somatério de termos H, calcula o valor de H
com N termos.
int -. float'''
    acum = 0
    for i in range(1, N + 1):
        H = 1/ i
        acum += H
    return round(acum,2)