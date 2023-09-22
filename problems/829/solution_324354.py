def soma_h(x):
    '''FUNCAO QUE CALCULA E RETORNA O VALOR DE H COM N TERMOS, RECEBDNO UM NUMERO DE ENTRADA.INT->FLOAT'''
    acum=0
    for i in range(1,x+1):
        H=1/i
        acum += H
    return round(acum,2)