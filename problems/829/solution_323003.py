def soma_h(n):
    '''Função que faz a somatória de uma sequência, dado N termos, e retorna este valor reduzido para duas casas decimais.
    int -> float'''
    acumular = 0
    for i in range(1, n + 1):
        H = 1 / i
        acumular += H
   	return round(acumular, 2)