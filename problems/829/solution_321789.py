def soma_h(N):
    """ funcao que recebe  um inteiro como entrada, calcula 
    H, sendo H uma expressao dada:1+1/2+1/3+..+1/N, e 
    retorna o valor de H com 2 casa decimais.
    entrada-> int
    saida-> float"""
    H=0
    for i in range(1,N+1):
        H= H+(1/i)
    return round(H,2)