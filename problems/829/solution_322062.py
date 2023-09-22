def soma_h(N):
    '''Retorna o valor da soma H (harmônica) até o termo N;
       int -> float'''
    soma_parcial = 0
    def termo_geral(N):
        return 1/N
    for x in range(1, N+1):
        soma_parcial += termo_geral(x)
    return round(soma_parcial, 2)